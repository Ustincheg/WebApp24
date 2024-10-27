from rest_framework import generics
from ..models import Films
from .serializers import SubjectSerializer, SubjectSerializer_Detail
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class SubjetListView(generics.ListAPIView):
    queryset = Films.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]

class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Films.objects.all()
    serializer_class = SubjectSerializer_Detail
    permission_classes = [IsAuthenticated ]


class SubjectCreateView(generics.CreateAPIView):
    queryset = Films.objects.all()
    serializer_class = SubjectSerializer_Detail
    permission_classes = [IsAdminUser, ]

class SubjectUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Films.objects.all()
    serializer_class = SubjectSerializer_Detail
    permission_classes = [IsAdminUser, ]