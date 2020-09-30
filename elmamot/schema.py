
from language import schema as language_schema
import graphene

class Query(language_schema.Query,graphene.ObjectType):
	pass

class Mutation(graphene.ObjectType, language_schema.Mutation):
	pass

schema = graphene.Schema(query = Query, mutation=Mutation)

