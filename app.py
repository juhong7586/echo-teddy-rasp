
from fastapi import FastAPI, File, UploadFile, Request
from teddy_bear_rasp import TeddyBearRasp
import shutil
import httpx 
import os
import uuid

app = FastAPI()
teddy_rasp = TeddyBearRasp()

@app.get("/")
async def home():
	return {"Hello": "World"}

	
@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
	UPLOAD_DIR = './'
	content = await file.read()
	filename = f"{str(uuid.uuid4())}.jpg"  # uuid로 유니크한 파일명으로 변경
	with open(os.path.join(UPLOAD_DIR, filename), "wb") as fp:
		fp.write(content)  # 서버 로컬 스토리지에 이미지 저장 (쓰기)
		
	return {"filename": filename}


# async def download_wav_file(url: str, save_path: str):
#     async with httpx.AsyncClient() as client:
#         response = await client.post(url)
#         response.raise_for_status()  # Raise an exception for HTTP errors

#         with open(save_path, "wb") as f:
#             f.write(response.content)
#         print(f"File saved to {save_path}")



# for test
@app.get("/speak")
async def speak(audio: UploadFile = File(...)):
	content = await audio.read()
	await teddy_rasp.speak(content)



if __name__ == "__main__":
	os.system('poetry run python3 listening.py')
	
