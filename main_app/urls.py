from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('recommendations/<int:recommendation_id>', views.recommendations_detail, name='detail'),
    path('recommendations/create/', views.add_recommendation, name='create'),
    path('recommendations/<int:pk>/update/', views.RecommendationUpdate.as_view(), name='update'),
    path('recommendations/<int:pk>/delete/', views.RecommendationDelete.as_view(), name='delete'),
    path('profile/', views.ProfileList.as_view(), name='profile_index'),
    path('profile/<int:pk>/', views.ProfileDetail.as_view(), name='profile_detail'),
    path('profile/create/', views.ProfileCreate.as_view(), name='profile_create'),
    path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profile_update'),
    path('profile/<int:pk>/delete/', views.ProfileDelete.as_view(), name='profile_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]