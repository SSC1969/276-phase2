import httpx                                  # HTTP client for calling user_service


class UserAPI:
    def __init__(self, base_url="http://localhost:8000"):   # default backend URL
        self.base = base_url                                # store for all requests


    # -----------------------
    # GET USER BY NAME
    # -----------------------
    async def get_by_name(self, username: str):
        async with httpx.AsyncClient() as client:           # create async client
            r = await client.get(f"{self.base}/v2/users/name/{username}")  # call endpoint
            if r.status_code == 404:                        # if user not found
                return None                                 # return None for UI
            return r.json()["user"]                         # return user dict


    # -----------------------
    # GET USER BY ID
    # -----------------------
    async def get_by_id(self, user_id: int):
        async with httpx.AsyncClient() as client:
            r = await client.get(f"{self.base}/v2/users/id/{user_id}")     # call endpoint
            if r.status_code == 404:
                return None
            return r.json()["user"]


    # -----------------------
    # CREATE USER
    # -----------------------
    async def create(self, name: str, email: str, password: str):
        body = {                                            # request body
            "name": name,
            "email": email,
            "password": password,
        }
        async with httpx.AsyncClient() as client:
            r = await client.post(f"{self.base}/v2/users/", json=body)     # call endpoint
            if r.status_code != 201:_
