from fastapi import FastAPI
app=FastAPI()

@app.get('/')
def root():
    return {"message":"helloworld"}

@app.post("/")
def creatpost():
    return {"message":"how are you!!!!"}
