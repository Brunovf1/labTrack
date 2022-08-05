from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


class MaterialbottleConfig(ModuleMixin, AppConfig):
    name = 'materialBottle'
    icon = '<i class="material-icons">settings_applications</i>'
    default_auto_field = 'django.db.models.AutoField'
