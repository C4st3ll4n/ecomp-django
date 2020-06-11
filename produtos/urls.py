
from django.urls import path
from produtos import views
app_name="produtos"
urlpatterns = [
    path('list/', views.list_products, name="list"),
    path('create/', views.create_product,  name="create"),
    path('update/<int:id>', views.update_product, name="update"),
    path('delete/<int:id>', views.delete_product, name="delete"),
]
