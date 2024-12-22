from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("", views.DishesList.as_view(), name="dish_list"),
    path("dishes/", views.DishesList.as_view(), name="dish_list"),
    path("dishes/<int:pk>", views.DishDetail.as_view(), name="dish_detail"),
    path("tags/", views.TagsList.as_view(), name="tags_list"),
    path("tags/<int:pk>", views.TagDetail.as_view(), name="tags_detail"),
    path("dishes/<str:tag>/", views.DishesByTagView.as_view(), name="dishes-by-tag"),
    # path("dishes/", views.dishes_list, name="dishes_list"),
    # path("home/", views.dishes_list, name="dishes_list"),
    # path("dish/<int:id>", views.dish_detail, name="dish"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
