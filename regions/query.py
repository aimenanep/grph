import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import *


class CountryNode(DjangoObjectType):
    dbid = graphene.ID(source='pk', required=True)
    class Meta:
        model = Country
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )

class RegionNode(DjangoObjectType):
    dbid = graphene.ID(source='pk', required=True)
    class Meta:
        model = Region
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'country': ['exact',],
        }
        interfaces = (relay.Node, )


class CityNode(DjangoObjectType):
    dbid = graphene.ID(source='pk', required=True)
    class Meta:
        model = City
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'region': ['exact',],
        }
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    all_countries=DjangoFilterConnectionField(CountryNode)
    all_regions=DjangoFilterConnectionField(RegionNode)
    all_cities=DjangoFilterConnectionField(CityNode)
