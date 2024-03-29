"""
URL configuration for first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from catalog.views import (CategoryViews, TagViews, GoodsViews, HelloViews, CategoryListViews, CategoryDetailView,
CategoryCreateView, CategoryUpdateView, CategoryDeleteView, GoodsUpdateView)
from payments.views import PaymentViews
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

Router = routers.DefaultRouter()
Router.register('category', CategoryViews)
Router.register('goods', GoodsViews)
Router.register('payments', PaymentViews)

schema_view = get_schema_view(
    openapi.Info(
        title='Catalog API',
        default_version='v2',
        description='Catalog API',
    ),
    public=True,
    #permission_classes=(pesmissions.AllowAny,),
)


urlpatterns = [
    path(r'jet/', include('jet.urls', 'jet')),
    path(r'jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('api/', include(Router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/tags', TagViews.as_view({'get': 'list'})),
    path('api-auth/', include('rest_framework.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),

    path('', HelloViews.as_view(), name='hello'),
    path('category-list', CategoryListViews.as_view(), name='category-list'),
    path("category_detail/<int:pk>/", CategoryDetailView.as_view(), name='category-detail'),
    path("category-create", CategoryCreateView.as_view(), name='category-create'),
    path("category-update/<int:pk>/", CategoryUpdateView.as_view(), name='category-update'),
    path("category_delete/<int:pk>/", CategoryDeleteView.as_view(), name='category_delete'),
    path("goods_update/<int:pk>/", GoodsUpdateView.as_view(), name='goods_update'),

    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("__debug__/", include("debug_toolbar.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
