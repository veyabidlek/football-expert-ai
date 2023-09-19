from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chatbot.urls')),  # Include chatbot app's URLs for the root URL
    path('chatbot/', include('chatbot.urls')),  # Include chatbot app's URLs with a prefix
]
