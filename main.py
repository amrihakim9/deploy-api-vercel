# import package
from fastapi import FastAPI, Request, Header, HTTPException

# bikin object
app = FastAPI()

API_KEY = "secret123" 

# isi headers
# - informasi metadata
#   - format file harus berupa apa
#   - ngasih tahu request/response berasal dari mana
#   - ngasih tahu os yang dipakai oleh client apa
# - untuk otentikasi
#   - untuk melakukan request -> masukin username & password
#   - untuk melakukan request -> harus menyertakan api key yang sesuai
# - dll

# bikin endpoint / -> home
@app.get('/')
def getHome():
    return {
        "message": "hello world"
    }

@app.get('/secret')
def getSecret(api_key: str = Header(None)):
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    return {
        "message": "this is top secret!!!"
    }

@app.get('/see-headers')
def readHeader(request: Request):
    # mengambil headers dari request
    headers = request.headers

    # informasi credential -> password, token, kunci enkripsi

    return {
        "message": "isi headers",
        "headers": headers.get('User-Agent'),
        "headers accept": headers.get('Accept')
    }