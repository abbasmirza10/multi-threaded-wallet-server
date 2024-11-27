import threading

class Wallet:
  def __init__(self):
    """Initialize an empty wallet."""
    self.resources = {}
    self.lock = threading.Lock()
    self.condition = threading.Condition(self.lock)

  def get(self, resource):
    """Returns the amount of a given `resource` in this wallet."""
    return self.resources.get(resource, 0)

  def change(self, resource, delta):
    """
    Modifies the amount of a given `resource` in this wallet by `delta`.
    - If `delta` is negative, this function MUST NOT RETURN until the resource can be satisfied.
      (This function MUST BLOCK until the wallet has enough resources to satisfy the request.)
    - Returns the amount of resources in the wallet AFTER the change has been applied.
    """
    with self.condition:
        while self.resources.get(resource, 0) + delta < 0:
            self.condition.wait()
        self.resources[resource] = self.resources.get(resource, 0) + delta
        self.condition.notify_all()
        return self.resources[resource]

  def try_change(self, resource, delta):
    """
    Like change, but if change would block
    this method instead leaves the resource unchanged and returns False.
    """
    with self.condition:
        if self.resources.get(resource, 0) + delta < 0:
            return False
        self.resources[resource] = self.resources.get(resource, 0) + delta
        self.condition.notify_all()
        return self.resources[resource]

  def transaction(self, **delta):
    """
    Like calling change(key, value) for each key:value in `delta`, except:
    - All changes are made at once. If any change would block, the entire transaction blocks.
      Only continues once *all* the changes can be made as one atomic action.
    - Returns a dict of {resource:new_value} for all resources in the transaction.
    """
    with self.condition:
        while True:
            for resource, delta_value in delta.items():
                if self.resources.get(resource, 0) + delta_value < 0:
                    break
            else:
                break
            self.condition.wait()
        for resource, delta_value in delta.items():
            self.resources[resource] = self.resources.get(resource, 0) + delta_value
        self.condition.notify_all()
        return self.resources.copy()