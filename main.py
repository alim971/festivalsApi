import json
from datetime import datetime

from fastapi import FastAPI, Query, Response
from typing import Annotated
import os

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.get("/festivals")
# async def get_festivals(response: Response):
#     response.headers["charset"] = "utf-8"
#     dir_path = './data'
#
#     # list to store files
#     res = []
#
#     # Iterate directory
#     for path in os.listdir(dir_path):
#         # check if current path is a file
#         filename = os.path.join(dir_path, path)
#         if os.path.isfile(filename):
#             file = open(filename, encoding='utf-8')
#             data = json.load(file)
#             try:
#                 end_date = datetime.strptime(data['endDate'], '%Y-%m-%dT%H:%M')
#             except:
#                 try:
#                     end_date = datetime.strptime(data['endDate'], '%Y-%m-%d %H:%M')
#                 except:
#                     try:
#                         end_date = datetime.strptime(data['endDate'], '%Y-%m-%d %H:%M:%S')
#                     except:
#                         end_date = datetime.strptime(data['endDate'], '%Y-%m-%d %H:%M:%S.%f')
#             if datetime.now() < end_date:
#                 res.append(data['name'])
#             file.close()
#     return {"festivals": res}
#
#
# @app.get("/festivals/")
# async def get_festivals(response: Response, festivals: Annotated[list[str] | None, Query()] = None):
#     dir_path = './data'
#     response.headers["charset"] = "utf-8"
#
#     # list to store files
#     res = []
#
#     # Iterate directory
#     for path in os.listdir(dir_path):
#         filename = os.path.join(dir_path, path)
#         if os.path.isfile(filename):
#             file = open(filename, encoding='utf-8')
#             data = json.load(file)
#             if data['name'] in festivals:
#                 res.append(data)
#             file.close()
#     return {"festivals": res}
