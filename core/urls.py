from django.urls import path
from core.views import hello, bye, sahifa, link_list, link_detail, link_create, link_update

urlpatterns = [
    path('/', hello),
    path('bye', bye),
    path('sahifa', sahifa),
    path('', link_list),
    path('<int:link_id>', link_detail),
    path('create', link_create),
    path('<int:link_id2>/update', link_update)
]
