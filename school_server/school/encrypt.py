import datetime
from school_server.settings import SECRET_KEY
import jwt

def create_jwt(username, password):
    encoded_jwt = jwt.encode({"username": username,
                              "password": password,
                              'timestamp': str(datetime.datetime.now())},
                             SECRET_KEY,
                             algorithm="HS256")
    return encoded_jwt
