from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Category',CategoryAPI)
router.register('sub-category',SubcategoryAPI)
router.register('Company',CompanyAPI)
router.register('product',ProductAPI)
# router.register('Registration',RegistrationView)
# router.register('Login',Login)


urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),

    path('Registration/',RegistrationView.as_view()),
    path('Login/',Login.as_view())

]
