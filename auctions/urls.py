from django.urls import path
from .views import CategoryListCreate, CategoryRetrieveUpdateDestroy, AuctionListCreate, AuctionRetrieveUpdateDestroy, BidListCreateView, BidDetailView

app_name="auctions"
urlpatterns = [
   path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroy.as_view(), name='category-detail'),
    path('', AuctionListCreate.as_view(), name='auction-list-create'),
    path('<int:pk>/', AuctionRetrieveUpdateDestroy.as_view(), name='auction-detail'),
    path('<int:id_auction>/bid/', BidListCreateView.as_view(), name='bid-list-create'),
    path('<int:id_auction>/bid/<int:pk>/', BidDetailView.as_view(), name='bid-detail'),
]
