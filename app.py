
from fastapi import FastAPI, File, UploadFile, Request
from teddy_bear_rasp import TeddyBearRasp


app = FastAPI()
teddy_rasp = TeddyBearRasp()

@app.get("/")
async def home():
	return {"Hello": "World"}

	
@app.post("/speak")
async def upload(audio: UploadFile = File(...)):
	await teddy_rasp.speak(audio)


# for test
@app.post("/listen")
async def listen(audio: UploadFile = File(...)):
	await teddy_rasp.speak(audio)
