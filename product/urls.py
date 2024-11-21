from django.urls import path
from product import views

urlpatterns = [
    path('category/', views.CategoryListAPIView.as_view(), name='category'),
    path('category/<int:pk>/', views.CategoryRetrieveAPIView.as_view(), name='category-retrieve'),
    path(
        'category/<int:category_id>/subcategory/',
        views.CategorySubCategoryListView.as_view(),
        name='category-subcategory-list'
    ),
    path('subcategory/', views.SubCategoryListAPIView.as_view(), name='subcategory'),
    path('subcategory/<int:pk>/', views.SubCategoryRetrieveAPIView.as_view(), name='category-retrieve'),
    path('', views.ProductCreateAPIView.as_view(), name='product-create'),
    path('business/', views.ProductBusinessUserAPIView.as_view(), name='product-business-get'),
    path(
        'subcategory/<int:subcategory_id>/product/',
        views.SubCategoryProductAPIView.as_view(),
        name='subcategory-product-list'
    ),
]
