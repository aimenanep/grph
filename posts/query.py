import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Post


class PostNode(DjangoObjectType):
    dbid = graphene.ID(source='pk', required=True)
    class Meta:
        model = Post
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    all_posts=DjangoFilterConnectionField(PostNode)
