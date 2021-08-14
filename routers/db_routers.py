class AuthRouter:
    route_app_labels = {
        'auth',
        'contenttypes',
        'sessions',
        'admin',
        'User',
        'staticfiles',
        'messages',
        'sites',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'crispy_forms',}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'users_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'users_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'users_db'
        return None


class Products:
    route_app_labels = {'Products'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'products_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'products_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'products_db'
        return None

