import logging
from fastapi import FastAPI
from routers import diagnose

# Configurar logs estructurados básicos
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("DiagnosticAgent")

app = FastAPI(
    title="Agente de Diagnóstico IA",
    description="Microservicio backend para acelerar el diagnóstico y la resolución de incidentes operativos",
    version="1.0.0"
)

# Registrar routers
app.include_router(diagnose.router)

@app.on_event("startup")
async def startup_event():
    logger.info("Iniciando el Agente de Diagnóstico IA...")

@app.get("/")
def read_root():
    return {"message": "Bienvenido al Agente de Diagnóstico IA. Visite /docs para la documentación de la API."}
