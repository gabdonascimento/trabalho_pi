import json
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import os

# Create an instance of FastAPI
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)


@app.post("/criar_time")
async def read_root(request: Request):
    request_body = await request.body()
    json_data = json.loads(request_body.decode("utf-8"))
    print("json_data: ", json_data)
    # ip_list.append(request.client.host)
    #  print("ip_list: ", ip_list)
    return {"message": "Hello, Alexandre!"}


if __name__ == "__main__":
    os.system("uvicorn main:app --reload")
