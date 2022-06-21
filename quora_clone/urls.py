from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('account.urls')),
    path('api/questions/',include('questions.urls')),
    path('api/answers/', include('answers.urls')),
]
