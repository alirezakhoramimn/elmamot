
from language import schema as language_schema
import graphene

class Query(language_schema.Query,graphene.ObjectType):
	pass



schema = graphene.Schema(query = Query)

