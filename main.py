from graphene import Schema, ObjectType, String, Int, Field

class UserType(ObjectType):
    id = Int()
    name = String()
    age = Int()  # Assuming age is an integer

class Query(ObjectType):
    user = Field(UserType, user_id=Int())

    users = [
        {"id": 1, "name": "ANdy", "age": 33},
        {"id": 2, "name": "Janme", "age": 43},
    ]
    @staticmethod
    def resolve_user(self, info, user_id):
        matched_users = [user for user in Query.users if user["id"] == user_id]
        return UserType(**matched_users[0]) if matched_users else None

schema = Schema(query=Query)

qql = '''
query{
    user(userId: 2)
    {
        id
        name
        age
    }
}
'''

if __name__ == "__main__":
    result = schema.execute(qql)
    print(result.data)
