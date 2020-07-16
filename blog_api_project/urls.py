
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from api.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('user-auth/', include('rest_framework.urls')),
    path('post/token/', jwt_views.TokenObtainPairView.as_view(), name= 'token_obtain_pair'),
    path('post/token/refresh/', jwt_views.TokenRefreshView.as_view(), name= 'token_refresh'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
