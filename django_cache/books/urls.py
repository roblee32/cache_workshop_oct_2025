from django.urls import path

from .views import cached_view, uncached_view, cached_template, another_view_using_cached_fragment, fine_grained_cache

urlpatterns = [
    path("uncached_view/", uncached_view, name="uncached_view"),
    path("cached_view/", cached_view, name="cached_view"),
    path("cached_template/", cached_template, name="cached_template"),
    path("another_cached_template/", another_view_using_cached_fragment, name="another_cached_template"),
    path("fine_grained_cache/", fine_grained_cache, name="fine_grained_cache"),
]

