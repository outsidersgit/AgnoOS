# AgnoOS

Plataforma multi-agente de fitness coaching construída com o framework Agno. Backend Python (FastAPI) com 3 agentes especializados + frontend Next.js para interface de chat.

## Estrutura do Projeto

```
AgnoOS/
├── gymOS/                  # Backend Python (FastAPI + Agno)
│   ├── app.py              # Entry point - FastAPI/Uvicorn (porta 7777)
│   ├── agents.py           # Definição dos 3 agentes
│   ├── gym.db              # SQLite - memória dos agentes
│   └── knowledge/          # Base de conhecimento (protocolos fitness)
├── agent-ui/               # Frontend Next.js
│   ├── src/
│   │   ├── app/            # Pages (App Router)
│   │   ├── components/     # Componentes React
│   │   │   ├── chat/       # ChatArea, Sidebar, Messages
│   │   │   └── ui/         # shadcn/ui components
│   │   ├── api/            # Cliente HTTP e rotas
│   │   ├── hooks/          # Custom hooks (streaming, chat, sessions)
│   │   ├── lib/            # Utilitários
│   │   ├── types/          # TypeScript types
│   │   └── store.ts        # Zustand store
│   └── package.json
└── agno_assist.py          # Agente auxiliar standalone
```

## Comandos

### Backend (gymOS)
```bash
# Iniciar servidor (porta 7777)
python gymOS/app.py
```

### Frontend (agent-ui)
```bash
cd agent-ui

# Dev server (porta 3000)
pnpm dev

# Validação completa (lint + format + typecheck)
pnpm validate

# Comandos individuais
pnpm lint:fix
pnpm format:fix
pnpm typecheck
pnpm build
```

## Stack

- **Backend**: Python 3.12, Agno 2.5, FastAPI, Claude Sonnet 4.5 (Anthropic), SQLite
- **Frontend**: Next.js 15, React 18, TypeScript, Tailwind CSS, Zustand, shadcn/ui, Framer Motion
- **Ferramentas dos agentes**: DuckDuckGo (pesquisa nutricional)

## Arquitetura

### Agentes (gymOS/agents.py)
1. **Avaliador Físico** - Coleta dados do aluno (idade, peso, altura, experiência), classifica nível fitness
2. **Montador de Treinos** - Cria planos de treino personalizados com periodização
3. **Consultor de Nutrição** - Planos nutricionais, cálculo de macros, acompanhamento de progresso

Todos usam Claude Sonnet 4.5, memória SQLite (últimas 5 interações), e instruções em português.

### Comunicação
- Frontend conecta ao backend via HTTP streaming (SSE)
- Endpoint configurável (default: `http://localhost:7777`)
- Auth opcional via Bearer token (`NEXT_PUBLIC_OS_SECURITY_KEY`)

### API Routes
- `GET /agents` - Lista agentes disponíveis
- `POST /agents/{id}/runs` - Executa agente (streaming)
- `GET /sessions` - Lista sessões
- `DELETE /sessions/{id}` - Remove sessão

## Convenções de Código

### Frontend
- **Componentes**: PascalCase (`ChatArea.tsx`, `MessageItem.tsx`)
- **Funções/hooks**: camelCase com prefixo `use` para hooks
- **Organização**: Feature-based directories em `components/`
- **UI base**: shadcn/ui em `components/ui/` (não editar diretamente, usar CLI)
- **State**: Zustand store centralizado em `store.ts`
- **Styling**: Tailwind CSS utilities, CVA para variants

### Backend
- Agentes definidos em `agents.py`, aplicação em `app.py`
- Knowledge base como arquivos `.txt` em `gymOS/knowledge/`
- Instruções dos agentes em português brasileiro

## CI/CD

GitHub Actions (`agent-ui/.github/workflows/validate.yml`) roda `pnpm validate` em todo push.
