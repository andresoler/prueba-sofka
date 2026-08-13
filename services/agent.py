import random
import asyncio
from typing import List
from schemas.diagnose import OperationalMetrics

class DiagnosticAgent:
    async def simulate_diagnosis(self, prompt: str, tools: List[str]) -> tuple[str, OperationalMetrics]:
        # Simulamos un tiempo de procesamiento asíncrono
        latency_ms = random.uniform(150.0, 800.0)
        await asyncio.sleep(latency_ms / 1000.0) # Convertimos a segundos
        
        # Simulamos el costo de tokens basado en la longitud del prompt
        estimated_token_cost = round(len(prompt) * 0.05, 2)
        
        # Simulamos una respuesta de diagnóstico
        if not tools:
            diagnosis_result = "No se proporcionaron herramientas de contexto. El diagnóstico es limitado, pero parece ser un problema de infraestructura general."
        elif "dynatrace_metrics" in tools or "azure_devops_logs" in tools:
            diagnosis_result = "He analizado las métricas y logs con las herramientas proporcionadas. Detecté un pico inusual de consumo de CPU provocado por un proceso huérfano. Recomiendo reiniciar el servicio afectado y escalar los recursos."
        else:
            diagnosis_result = f"Se evaluó la situación utilizando {', '.join(tools)}. Todo parece estar dentro de los umbrales normales, aunque sugiero mantener monitoreo activo."
            
        metrics = OperationalMetrics(
            latency_ms=round(latency_ms, 2),
            estimated_token_cost=estimated_token_cost
        )
        
        return diagnosis_result, metrics

# Instancia global del agente
agent = DiagnosticAgent()
