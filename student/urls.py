from django.conf.urls import url,include
from rest_framework import routers

from management.views import StudentView

router = routers.SimpleRouter()
router.register(r'student', StudentView)

urlpatterns = router.urls
