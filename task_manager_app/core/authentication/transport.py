from  fastapi_users.authentication import BearerTransport

# TODO
bearer_transport = BearerTransport(tokenUrl="/auth/jwt/login")