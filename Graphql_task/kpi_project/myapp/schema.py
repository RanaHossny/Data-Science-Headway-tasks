import graphene
from .quary import Query
from .mutation import Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
