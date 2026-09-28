class PermissionManager:
    SAFE = "safe"
    DANGEROUS = "dangerous"

    def __init__(self):
        self._permissions = {}

    def set_permission(self, tool_name, permission):
        if permission not in (self.SAFE, self.DANGEROUS):
            return False

        self._permissions[tool_name] = permission
        return True

    def get_permission(self, tool_name):
        return self._permissions.get(tool_name, self.DANGEROUS)

    def is_allowed(self, tool_name, confirmed=False):
        permission = self.get_permission(tool_name)

        if permission == self.SAFE:
            return True

        return confirmed
