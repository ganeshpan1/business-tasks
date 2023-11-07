# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('perform_operation/<str:operation>/', views.perform_operation, name='perform_operation'),
#     path('perform_operation/<str:operation>/<int:pk>/', views.perform_operation, name='perform_operation'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('perform_operation/<str:operation>/', views.perform_operation, name='perform_operation'),
    path('perform_operation/<str:operation>/<int:pk>/', views.perform_operation, name='perform_operation'),
    # path('perform_operation/get_business/<int:id>/', views.get_business, name='get_business'),
]
