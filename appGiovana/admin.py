from django.contrib import admin
from .models import Dogs \\importa a classe "Dogs" criada em models 
from .models import Metas \\importa a classe "Metas" criada em models 

admin.site.register(Dogs) \\registra no página de acesso do administrador a classe "Dogs", para que seja possível editar a classe por lá
admin.site.register(Metas) \\registra no página de acesso do administrador a classe "Metas", para que seja possível editar a classe por lá
