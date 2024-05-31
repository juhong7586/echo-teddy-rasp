
from fastapi import FastAPI, File, UploadFile, Request
from teddy_bear_rasp import TeddyBearRasp
import shutil

app = FastAPI()
teddy_rasp = TeddyBearRasp()

@app.get("/")
async def home():
	return {"Hello": "World"}

	
@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
	with open(f"received_{file.filename}", "wb") as buffer: 
		shutil.copyfileobj(file.file, buffer)
		


# for test
@app.post("/listen")
async def listen(audio: UploadFile = File(...)):
	content = await audio.read()
	await teddy_rasp.speak(content)
