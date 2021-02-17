import graphene
from graphene_django.rest_framework.mutation import SerializerMutation
from .serializers import CategorySerializer
from .models import Category

class CategoryMutation(SerializerMutation):
    class Meta:
        serializer_class = CategorySerializer
        model_operations = ['create', 'update']
        lookup_field = 'id'

    @classmethod
    def get_serializer_kwargs(cls, root, info, **input):
        print(input)
        if 'id' in input:
            instance=Category.objects.get(id=input['id'])
            if instance:
                return {'instance': instance, 'data': input, 'partial': True}

            else:
                raise http.Http404

        return {'data': input, 'partial': True}

class Mutation(graphene.ObjectType):
    update_category = CategoryMutation.Field()
