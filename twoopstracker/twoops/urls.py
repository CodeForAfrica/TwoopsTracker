from django.urls import path

from .views import (
    AccountsList,
    SingleTwitterList,
    TweetSearchesView,
    TweetSearchView,
    TweetsGraphView,
    TweetsView,
)

urlpatterns = [
    path("tweets/", TweetsView.as_view(), name="tweets"),
    path("tweets/graph", TweetsGraphView.as_view(), name="tweets_graph"),
    path("tweets/searches", TweetSearchesView.as_view(), name="tweets_searches"),
    path(
        "tweets/searches/<pk>",
        TweetSearchView.as_view(),
        name="single_saved_search",
    ),
    path("lists/", AccountsList.as_view(), name="accounts_list"),
    path("lists/<pk>", SingleTwitterList.as_view(), name="single_account_list"),
]
