from agno.os import AgentOS
from agents import avaliador, treinador, nutricionista

# Criar AgentOS com os 3 agentes especializados
agent_os = AgentOS(
    agents=[avaliador, treinador, nutricionista]
)

# Exportar app FastAPI
app = agent_os.get_app()

if __name__ == "__main__":
    import os
    import uvicorn
    port = int(os.environ.get("PORT", 7777))
    host = os.environ.get("HOST", "127.0.0.1")
    uvicorn.run("app:app", host=host, port=port, reload=True)
