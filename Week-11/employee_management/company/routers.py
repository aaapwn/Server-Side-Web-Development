# company/routers.py
class CompanyRouter:
    route_app_labels = {"company"}
    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "db2"
        return None
    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "db2"
        return None
    def allow_relation(self, obj1, obj2, **hints):
        return True
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True
