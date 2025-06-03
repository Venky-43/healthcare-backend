from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.auth_views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views.patient_views import PatientViewSet
from api.views.doctor_views import DoctorViewSet
from api.views.mapping_views import MappingViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'doctors', DoctorViewSet, basename='doctor')
router.register(r'mappings', MappingViewSet, basename='mapping')

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
    path('', include(router.urls)),
]