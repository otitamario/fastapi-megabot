from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from chatbot import chatbot

megabot=chatbot()
megabot.init()
megabot.training()


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/get")
def get_bot_response(msg: str):
    return str(megabot.get_reply(msg))


if __name__ == "__main__":
    uvicorn.run("app:app")