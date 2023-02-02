# from django.urls import path
# from rest_framework.routers import DefaultRouter,SimpleRouter
# from rest_framework import routers
# router = DefaultRouter()
# from .views import MainViewSet

# router.register(r'', MainViewSet, basename='maincategory')
# urlpatterns = router.urls

# router = routers.SimpleRouter()
# urlpatterns += router.urls



# router = routers.DefaultRouter()
# router.register(r'custom-viewset', MainViewSet)
# # router.register(r'model-viewset', ItemModelViewSet) # newly registered ViewSet

# urlpatterns = [
#     path('', MainViewSet.as_view()),

# ]
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.SubCategoryViewSet.as_view() ),
    path('<int:pk>/', views.MainViewSet.as_view()),
    path('sub/',views.MainViewSet.as_view() ),
            
]
