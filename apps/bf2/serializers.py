from rest_framework.serializers import ListSerializer
from entity.serializers import BaseSerializerV2
from bf2.pagination import BadgrLimitOffsetPagination

class LimitOffsetPaginatedListSerializer(ListSerializer):
    def __init__(self, queryset, request, ordering='updated_at', *args, **kwargs):
        self.paginator = BadgrLimitOffsetPagination(ordering=ordering)
        self.page = self.paginator.paginate_queryset(queryset, request)
        super(LimitOffsetPaginatedListSerializer, self).__init__(data=self.page, *args, **kwargs)

    def to_representation(self, data):
        representation = super(LimitOffsetPaginatedListSerializer, self).to_representation(data)
        envelope = BaseSerializerV2.response_envelope(result=representation,
                                                      success=True,
                                                      description='ok')
        envelope['pagination'] = self.paginator.get_page_info()
        return envelope

    @property
    def data(self):
        return super(ListSerializer, self).data

