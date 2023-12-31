import asyncio
import logging
from fastapi import HTTPException, status, FastAPI
import requests
import random
from mangum import Mangum
import uvicorn
import requests
from starlette.types import ASGIApp

random.seed(54321)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

app = FastAPI()
# app: ASGIApp = FastAPI(on_startup=[_startup_event])
handler = Mangum(app)

@app.get("/")
async def read_root():
    logger.info(" INFO logging test ")
    logger.warning(" WARNING test ")
    logger.error(" ERROR log test")
    return {"Hello": "World"}

@app.get("/ping")
async def health_check():
    logger.info("This is message /ping")
    return "ping"

@app.get("/internal-api")
def internal_api():
    logger.info("This is message start /internal-pi ")
    response = requests.get(f"https://google.com")
    status_code_response = response.status_code
    content_response = response.content
    response.close()
    logger.info("This is message close /internal-API ")
    message = f" 'statis code:' + {status_code_response}  + content: + {content_response} "
    return message

@app.get("/external-api")
def internal_api():
    logger.info("This is message start /external-API")
    response = requests.get(f"hhttps://google.com")
    status_code_response = response.status_code
    content_response = response.content
    response.close()
    logger.info("This is message close /internal-pi ")
    message = f" 'statis code:' + {status_code_response}  + content: + {content_response} "
    return message