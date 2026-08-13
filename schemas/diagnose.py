from pydantic import BaseModel, Field
from typing import List, Optional

class DiagnoseRequest(BaseModel):
    user_id: str = Field(..., description="ID del usuario que solicita el diagnóstico")
    prompt: str = Field(..., description="Descripción del incidente en lenguaje natural")
    context_tools: List[str] = Field(default_factory=list, description="Lista de herramientas a utilizar")

class OperationalMetrics(BaseModel):
    latency_ms: float = Field(..., description="Latencia de la operación en milisegundos")
    estimated_token_cost: float = Field(..., description="Costo estimado en tokens")

class DiagnoseResponse(BaseModel):
    sanitized_prompt: str = Field(..., description="Prompt sanitizado sin datos PII")
    executed_tools: List[str] = Field(..., description="Herramientas que se ejecutaron")
    diagnosis_result: str = Field(..., description="Resultado simulado del diagnóstico")
    metrics: OperationalMetrics = Field(..., description="Métricas operacionales de la ejecución")
