from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from api.views import UserViewSet, GroupViewSet, ChangePasswordView, CategoryView, UserGroupView, MeetingViewSet, \
    UserMeetingView, DeleteGroupParticipantView, DeleteMeetingParticipantView

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
                  path('users/<int:pk>/groups', UserGroupView.as_view(), name="user_groups"),
                  path('users/<int:pk>/meetings', UserMeetingView.as_view(), name="user_meetings"),
                  path('group_participants/<int:pk>/', DeleteGroupParticipantView.as_view(),
                       name="exit_user_from_group"),
                  path('meeting_participants/<int:pk>/', DeleteMeetingParticipantView.as_view(),
                       name="exit_user_from_meeting"),
              ] + router.urls
