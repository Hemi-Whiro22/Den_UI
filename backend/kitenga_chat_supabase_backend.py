
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

# Load Supabase from env
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

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
