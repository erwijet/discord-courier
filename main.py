from fastapi import FastAPI
from pydantic import BaseModel
from requests import post

class DiscordWebhookPayload(BaseModel):
    content: str

app = FastAPI()
ok = { "ok": True } 

@app.get("/")
def index():
    return ok

@app.post("/{channel}/{title}")
def relay(channel: str, title: str, payload: DiscordWebhookPayload):
    post(f"https://ntfy.sh/{channel}?title={title}", data=payload.content, headers={"Markdown": "yes"})
    return ok

