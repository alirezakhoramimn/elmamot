
from language import schema as language_schema
import graphene

import graphql_jwt

class Query(language_schema.Query,graphene.ObjectType):
	pass

class Mutation(language_schema.Mutation,graphene.ObjectType ):
	token_auth = graphql_jwt.ObtainJSONWebToken.Field()
	verify_token = graphql_jwt.Verify.Field()
	refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query = Query, mutation=Mutation)

