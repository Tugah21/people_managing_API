#just an Example

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return {'Hello': 'world'}

@app.post('/')
def hello_post():
    return {'Success': 'yOU PosTeD!'}

@app.get('/something')
def something():
    return {'Data': 'Something'}