from rest_framework import generics
from .models import Category, Auction, Bid
from .serializers import CategoryListCreateSerializer, CategoryDetailSerializer, AuctionListCreateSerializer, AuctionDetailSerializer, BidSerializer

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListCreateSerializer

class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer

class AuctionListCreate(generics.ListCreateAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionListCreateSerializer

class AuctionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionDetailSerializer

class BidListCreateView(generics.ListCreateAPIView):
    serializer_class = BidSerializer

    def get_queryset(self):
        return Bid.objects.filter(auction=self.kwargs['id_auction'])

    def perform_create(self, serializer):
        auction = Auction.objects.get(id=self.kwargs['id_auction'])
        serializer.save(auction=auction)

class BidDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BidSerializer

    def get_queryset(self):
        return Bid.objects.filter(id=self.kwargs['pk'], auction=self.kwargs['id_auction'])