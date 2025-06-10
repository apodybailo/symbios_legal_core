from fastapi import APIRouter, HTTPException
from src.tasks.generate import generate_contract_task, generate_lawsuit_task

router = APIRouter()

@router.post("/contract", summary="Generate contract")
def generate_contract(body: dict):
    task = generate_contract_task.delay(body["client_id"], body["template_name"])
    return {"task_id": task.id}

@router.post("/lawsuit", summary="Generate lawsuit")
def generate_lawsuit(body: dict):
    task = generate_lawsuit_task.delay(body["case_id"], body["template_name"])
    return {"task_id": task.id}