from django.urls import path, include
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('admin/', admin.site.urls),
    path('', include('learning_logs.urls')),  
    path('recipes/', include('recipes.urls')),
]

