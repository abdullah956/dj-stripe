# project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payments/', include('stripes.urls')),  # Include the Stripe URLs here
]
