import os
from agno.os import AgentOS
from agents import avaliador, treinador, nutricionista

# Origens permitidas para CORS
_cors_origins = [
    "http://localhost:3000",
    "https://laudable-sparkle-production-0a8a.up.railway.app",
]
if extra := os.environ.get("CORS_ORIGINS"):
    _cors_origins.extend(extra.split(","))

# Criar AgentOS com os 3 agentes especializados
agent_os = AgentOS(
    agents=[avaliador, treinador, nutricionista],
    cors_allowed_origins=_cors_origins,
)

# Exportar app FastAPI
app = agent_os.get_app()

if __name__ == "__main__":
    import os
    import uvicorn
    port = int(os.environ.get("PORT", 7777))
    host = os.environ.get("HOST", "127.0.0.1")
    uvicorn.run("app:app", host=host, port=port, reload=True)
