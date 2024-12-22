from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView

from .models import Dish, Tag
from .serializers import DishSerializer, TagSerializer

from rest_framework import generics, viewsets


class DishesList(generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    print(queryset[0].owner)
    serializer_class = DishSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# class DishDetail(generics.RetrieveAPIView, generics.UpdateAPIView):
class DishDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    lookup_field = "pk"


class TagsList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "pk"


class DishesByTagView(generics.ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    filterset_fields = ["food_tags"]

    def get_queryset(self):
        tag_name = self.kwargs["tag"]
        queryset = super().get_queryset()
        if tag_name:
            return queryset.filter(food_tags__name=tag_name)
        else:
            return super().get_queryset()


# class DishesList(APIView):
#     def get(self, request, format=None):
#         dishes = Dish.objects.all()
#         serializer = DishSerializer(dishes, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = DishSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status.status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "POST"])
# @permission_classes((permissions.AllowAny,))
# def dishes_list(request, format=None):
#     if request.method == "GET":
#         dishes = Dish.objects.all()
#         # tags = Tag.objects.all()
#         serializer = DishSerializer(dishes, context={"request": request}, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = DishSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status.status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "PUT", "DELETE"])
# def dish_detail(request, pk, format=None):
#     try:
#         dish = Dish.objects.get(pk=pk)
#     except Dish.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = DishSerializer(dish)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = DishSerializer(dish, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status.status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         dish.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# def home(request):
#     dishes = Dish.objects.all()
#     tags = Tag.objects.all()
#     context = {"dishes": dishes, "tags": tags}
#     return render(request, "index.html", context=context)


# def dish(request, id):
#     dish = get_object_or_404(Dish, pk=id)
#     return render(request, "dish.html", {"dish": dish})
