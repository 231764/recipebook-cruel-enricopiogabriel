from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('ledger.urls', namespace="ledger")),  # Include ledger URLs
    path('admin/', admin.site.urls),
]