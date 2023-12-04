from django.urls import path
from . import views 

urlpatterns = [ path("register/", views.register, name = 'register'),
                path("logout/", views.custom_logout, name = 'logout'),           
                path("profile/", views.profile, name = 'profile'),           
                path("profile-update/", views.profile_update, name = 'profile_update'),
                path("staff/", views.staff, name = 'staff'),
                path("staff-detail-<int:pk>/", views.staff_detail, name = 'staff_detail'),
                path("staff-delete-<int:pk>/", views.staff_delete, name = 'staff_delete'),
                path("staff-active-<int:pk>/", views.staff_active, name = 'staff_active'),
                path("staff-staff-<int:pk>/", views.staff_staff, name = 'staff_staff'),
                path("staff-super-<int:pk>/", views.staff_super, name = 'staff_super')
]