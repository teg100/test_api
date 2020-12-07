from rest_framework import generics, views
from .serializers import *
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .tasks import update_view_count
from django.db import transaction

class PageListView(generics.ListAPIView):
    queryset = Page.objects.select_related()
    serializer_class = PageListSerializer


# class PageDetail(generics.RetrieveAPIView):
#     queryset = Page.objects.all()
#     serializer_class = PageSerializer
#
#     def get(self, request, pk, *args, **kwargs):
#         page = Page.objects.get(pk=pk).select_related()


class PageDetail(views.APIView):

    def get(self, request, pk, format=None):
        page = get_object_or_404(Page, pk=pk)
        serializer = PageSerializer(page)
        update_view_count.delay(pk)
        return Response(serializer.data)