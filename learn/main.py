from fastapi import FastAPI
import uvicorn

my_awesome_api = FastAPI()


@my_awesome_api.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == '__main__':
    uvicorn.run(my_awesome_api,
                host='127.0.0.1',
                port=8080)