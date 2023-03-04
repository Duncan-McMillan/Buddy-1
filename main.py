from fastapi import FastAPI
from fastapi.responses import FileResponse 

app = FastAPI()

@app.get("/")
def root():
    return FileResponse("Images/buddy-1.jpg")

