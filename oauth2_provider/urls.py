from django.urls import path
from django.urls import re_path

from . import views


app_name = "oauth2_provider"


base_urlpatterns = [
    path("authorize/", views.AuthorizationView.as_view(), name="authorize"),
    path("token/", views.TokenView.as_view(), name="token"),
    path("revoke_token/", views.RevokeTokenView.as_view(), name="revoke-token"),
    path("introspect/", views.IntrospectTokenView.as_view(), name="introspect"),
]


management_urlpatterns = [
    # Application management views
    path("applications/", views.ApplicationList.as_view(), name="list"),
    path("applications/register/", views.ApplicationRegistration.as_view(), name="register"),
    re_path(r"^applications/(?P<pk>[\w-]+)/$", views.ApplicationDetail.as_view(), name="detail"),
    re_path(r"^applications/(?P<pk>[\w-]+)/delete/$", views.ApplicationDelete.as_view(), name="delete"),
    re_path(r"^applications/(?P<pk>[\w-]+)/update/$", views.ApplicationUpdate.as_view(), name="update"),
    # Token management views
    path("authorized_tokens/", views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
    re_path(
        r"^authorized_tokens/(?P<pk>[\w-]+)/delete/$",
        views.AuthorizedTokenDeleteView.as_view(),
        name="authorized-token-delete",
    ),
]

oidc_urlpatterns = [
    re_path(
        r"^\.well-known/openid-configuration/$",
        views.ConnectDiscoveryInfoView.as_view(),
        name="oidc-connect-discovery-info",
    ),
    re_path(r"^\.well-known/jwks.json$", views.JwksInfoView.as_view(), name="jwks-info"),
    path("userinfo/", views.UserInfoView.as_view(), name="user-info"),
]


urlpatterns = base_urlpatterns + management_urlpatterns + oidc_urlpatterns
