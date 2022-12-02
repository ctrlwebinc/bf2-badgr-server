from rest_framework.pagination import LimitOffsetPagination

class BadgrLimitOffsetPagination(LimitOffsetPagination):
    ordering = '-created_at'

    def __init__(self, ordering=None, page_size=None):
        super(BadgrLimitOffsetPagination, self).__init__()