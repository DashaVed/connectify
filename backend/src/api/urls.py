from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from api.views import UserViewSet, GroupViewSet, ChangePasswordView, CategoryView, UserGroupView, MeetingViewSet, \
    UserMeetingView, AddUserGroupView, AddUserMeetingView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'meetings', MeetingViewSet, basename='meetings')

urlpatterns = [
                  path('schema/', SpectacularAPIView.as_view(), name='schema'),
                  path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
                  path('auth/', include('djoser.urls')),
                  path('auth/', include('djoser.urls.jwt')),
                  path('auth/change/password/<int:pk>', ChangePasswordView.as_view(), name="change_password"),
                  path('categories/', CategoryView.as_view(), name="category"),
                  path('users/<int:pk>/groups', UserGroupView.as_view(), name="user_group"),
                  path('users/<int:pk>/meetings', UserMeetingView.as_view(), name="user_meeting"),
                  path('groups/<int:pk>/add/user', AddUserGroupView.as_view(), name="add_user_to_group"),
                  path('meetings/<int:pk>/add/user', AddUserMeetingView.as_view(), name="add_user_to_group"),
              ] + router.urls
