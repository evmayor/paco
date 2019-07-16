"""Pacioli URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url, include
from rest_framework import routers
from apps.pacioliApp import views
from apps.pacioliApp.views import PurchaseList

router = routers.DefaultRouter()
router.register(r'plan',views.planViewSet)
#router.register(r'purchases',views.PurchaseList)
#router.register(r'purchases/(?P<neducat>.+)/$', PurchaseList.as_view(), base_name='put-something-here')

router.register(r'milista',views.listado,base_name='put-something-here')
router.register(r'milistab/educat',views.listadob,base_name='put-something-here-b')
#libro diario
router.register(r'diario',views.libroDiarioViewSet)
#asientoMaxViewSet
router.register(r'asiento',views.asientoMaxViewSet,base_name='put-something-here-c')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'',include(router.urls)),
    

]
