from django.urls import path

from api.views import DirectionList, DirectionDetail

urlpatterns = [
    path('features/', DirectionList.as_view(), name='directions_list'),
    path('features/<int:pk>', DirectionDetail.as_view(), name='directions_detail')
]