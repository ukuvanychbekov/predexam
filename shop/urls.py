from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter


from . import views

router = DefaultRouter()
router.register('category', views.CategoryViewSet, basename='shop')

urlpatterns = [
    path('', include(router.urls)),
    path('category/<int:category_id>/items/', views.ItemListCreateAPIView.as_view()),
    path('category/<int:category>/items/<int:pk>/', views.ItemRetrieveUpdateDestroyAPIView.as_view()),
    path('category/<int:category>/items/<int:pk>/order/', views.OrderListCreateAPIView.as_view()),
    path('category/<int:category>/items/<int:pk>/order/<int:id>', views.OrderRetrieveUpdateDestroyAPIView.as_view()),
   ]
