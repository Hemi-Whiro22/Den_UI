
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import os
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatInput(BaseModel):
    message: str

memory_file = "memory/kitenga_memory.json"

if not os.path.exists(memory_file):
    with open(memory_file, "w") as f:
        json.dump([], f)

@app.post("/chat")
async def chat(input: ChatInput):
    with open(memory_file, "r") as f:
        memory = json.load(f)

    # Simulate basic AI response
    response = f"I hear you, and I’m with you: {input.message}"

    memory.append({
        "timestamp": datetime.now().isoformat(),
        "user": input.message,
        "kitenga": response
    })

    with open(memory_file, "w") as f:
        json.dump(memory, f, indent=2)

    return {"response": response}
