from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import base64
import openai
import os
from supabase import create_client, Client

app = FastAPI()
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import os
from datetime import datetime
from supabase import create_client, Client

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
import os

SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "")

# Add debug print for confirmation (for dev only)
print("🔑 SUPABASE_KEY LOADED LENGTH:", len(SUPABASE_KEY))
)

class ChatInput(BaseModel):
    message: str
    user_id: str = "default_user"

memory_file = "memory/kitenga_memory.json"

if not os.path.exists(memory_file):
    with open(memory_file, "w") as f:
        json.dump([], f)

@app.post("/chat")
async def chat(input: ChatInput):
    with open(memory_file, "r") as f:
        memory = json.load(f)

    response = f"I hear you, and I’m with you: {input.message}"

    entry = {
        "timestamp": datetime.now().isoformat(),
        "user": input.message,
        "kitenga": response
    }
    memory.append(entry)

    with open(memory_file, "w") as f:
        json.dump(memory, f, indent=2)

    # Save to Supabase
    try:
        supabase.table("messages").insert({
            "user_id": input.user_id,
            "message": input.message,
            "response": response
        }).execute()
    except Exception as e:
        print("Supabase insert error:", e)

    return {"response": response}


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
