from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from api.views import UserViewSet, GroupViewSet, ChangePasswordView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'groups', GroupViewSet, basename='groups')

urlpatterns = [
                  path('schema/', SpectacularAPIView.as_view(), name='schema'),
                  path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
                  path('auth/', include('djoser.urls')),
                  path('auth/', include('djoser.urls.jwt')),
                  path('auth/change/password/<int:pk>', ChangePasswordView.as_view(), name="change_password")
              ] + router.urls
