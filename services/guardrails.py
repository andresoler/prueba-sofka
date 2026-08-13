import re
from fastapi import HTTPException

# Patrones para detectar datos sensibles
IPV4_PATTERN = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
API_KEY_PATTERN = r'(?i)(?:api_key|token|secret)[\s:=]+([a-zA-Z0-9_\-]+)'

# Lista de frases de inyección maliciosa
PROMPT_INJECTION_PATTERNS = [
    "ignore previous instructions",
    "forget everything",
    "disregard",
    "bypassing",
    "system prompt"
]

class SecurityGuardrails:
    def sanitize_pii(self, prompt: str) -> str:
        # Enmascarar direcciones IP
        sanitized = re.sub(IPV4_PATTERN, "[REDACTED_IP]", prompt)
        
        # Enmascarar posibles API Keys o tokens
        # Aquí buscamos el patrón y reemplazamos solo el valor
        def replace_api_key(match):
            full_match = match.group(0)
            key_value = match.group(1)
            return full_match.replace(key_value, "[REDACTED_API_KEY]")
            
        sanitized = re.sub(API_KEY_PATTERN, replace_api_key, sanitized)
        
        return sanitized

    def check_prompt_injection(self, prompt: str):
        prompt_lower = prompt.lower()
        for pattern in PROMPT_INJECTION_PATTERNS:
            if pattern in prompt_lower:
                raise HTTPException(
                    status_code=400,
                    detail="Solicitud rechazada: Se ha detectado un posible intento de inyección en el prompt."
                )

# Instancia global para usar en la aplicación
guardrails = SecurityGuardrails()
