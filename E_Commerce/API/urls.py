from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('Category',CategoryAPI)
router.register('sub-category',SubcategoryAPI)
router.register('Company',CompanyAPI)
router.register('product',ProductAPI)
# router.register('Registration',RegistrationView)
# router.register('Login',Login)

product_router = routers.NestedDefaultRouter(router,"product",lookup="product")
product_router.register("reviews",ReviewAPI,basename="product-reviews")
category_router = routers.NestedDefaultRouter(router,"Category",lookup="Category")
category_router.register("products",FilterProductByCategory,basename="product-category")

# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
    path('', include(category_router.urls)),

    path('Registration/',RegistrationView.as_view()),
    path('Login/',Login.as_view())

]
