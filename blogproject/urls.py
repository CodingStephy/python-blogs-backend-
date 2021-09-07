from django.urls import path, include
from rest_framework import routers
from blogs.views import BlogViewSet

# create the router
router = routers.DefaultRouter()
# register our viewsets
router.register(r'blog', BlogViewSet) # register /todos

print(router)


urlpatterns = [
    path("", include(router.urls))
]