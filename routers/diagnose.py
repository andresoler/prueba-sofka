from fastapi import APIRouter
from schemas.diagnose import DiagnoseRequest, DiagnoseResponse
from services.guardrails import guardrails
from services.agent import agent

router = APIRouter(
    prefix="/api/v1/agent",
    tags=["Agent"]
)

@router.post("/diagnose", response_model=DiagnoseResponse)
async def diagnose_incident(request: DiagnoseRequest):
    # 1. Capa de Gobernanza: Verificar inyección de prompts
    guardrails.check_prompt_injection(request.prompt)
    
    # 2. Capa de Gobernanza: Sanitizar datos sensibles (PII)
    sanitized_prompt = guardrails.sanitize_pii(request.prompt)
    
    # 3. Orquestación: Ejecutar el agente con el prompt limpio
    diagnosis_result, metrics = await agent.simulate_diagnosis(
        prompt=sanitized_prompt, 
        tools=request.context_tools
    )
    
    # 4. Respuesta estructurada
    return DiagnoseResponse(
        sanitized_prompt=sanitized_prompt,
        executed_tools=request.context_tools,
        diagnosis_result=diagnosis_result,
        metrics=metrics
    )
