from django.urls import path
# from .views import MacbookListView, MacbookDetailView, MacbookDestroyView, MacbookUpdateView, MacbookCreateView
#
# urlpatterns = [
#     path('', MacbookListView.as_view(), name='mac_list'),
#     path('detail/<int:pk>', MacbookDetailView.as_view(), name='mac-detail'),
#     path('delete/<int:pk>', MacbookDestroyView.as_view(), name='mac-delete'),
#     path('update/<int:pk>', MacbookUpdateView.as_view(), name='mac-update'),
#     path('create/', MacbookCreateView.as_view(), name='mac-create')
# ]

# from .views import MacbookApiView, MacbookPKApiView
from .views import ListCreateApi, DetailUpdateDeleteApi
urlpatterns = [
    path('', ListCreateApi.as_view(), name='mac-list'),
    path('detail/<int:pk>/', DetailUpdateDeleteApi.as_view(), name='mac-detail')
]