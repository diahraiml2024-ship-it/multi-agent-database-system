from fastapi import FastAPI
from pydantic import BaseModel

from agents.planner_agent import PlannerAgent
from agents.schema_agent import SchemaAgent
from core.orchestrator import AgentOrchestrator

app = FastAPI(
    title="Multi-Agent Intelligent Database System",
    version="1.0.0"
)

# Initialize agents
planner = PlannerAgent()
schema_agent = SchemaAgent()

# Create orchestrator pipeline
orchestrator = AgentOrchestrator(
    agents=[
        planner,
        schema_agent
    ]
)
import os

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)

class QueryRequest(BaseModel):
    query: str


@app.get("/")
def read_root():
    return {"message": "System is running"}


@app.post("/query")
def process_query(request: QueryRequest):
    data = {"query": request.query}

    result = orchestrator.run(data)

    return result