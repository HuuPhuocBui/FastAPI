from fastapi import FastAPI

#tao API instance
app = FastAPI()

#di tao 1 api
@app.get("/hello") # /hello: route định tuyến
def read_root():
    return {"message": "Hello World"}