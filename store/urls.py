from django.urls import path

from . import views

urlpatterns = [
    path("add/", views.add_mobile, name="add_mobile"),
    path("list/", views.list_mobiles, name="list_mobiles"),
    path("report/korea_nationality/", views.report_korea_nationality, name="report_korea_nationality"),
    path("report/brand_mobiles/", views.report_brand_mobiles, name="report_brand_mobiles"),
    path(
        "report/same_country_nationality/",
        views.report_same_country_nationality,
        name="report_same_country_nationality",
    ),
]
