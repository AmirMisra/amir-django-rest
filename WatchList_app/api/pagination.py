from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class WatchListPagination(PageNumberPagination):
    page_size = 3
    # page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 4
    # last_page_strings = 'end'


class WatchListLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    limit_query_param = 'limit'
    offset_query_param = 'start'


class WatchListCursorPagination(CursorPagination):
    page_size = 3
    ordering = 'created'
    cursor_query_param = 'record'
