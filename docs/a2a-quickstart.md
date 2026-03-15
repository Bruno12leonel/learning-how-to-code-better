# Fase 2: A2A Com AgentExecutor

## O Que Foi Adicionado

- um agente remoto A2A em `src/remote_a2a/study_explainer/agent.py`
- um `StudyConceptAgentExecutor` que implementa `execute()` e `cancel()`
- o agente ADK principal agora consome esse remoto com `RemoteA2aAgent`

## Arquitetura

- `src/agent/agent.py`: agente ADK que conversa com o usuario
- `src/tools/study_lookup.py`: consulta local curta
- `src/remote_a2a/study_explainer/agent.py`: servidor remoto A2A
- `src/core/study_explainer.py`: logica do dominio usada pelo executor remoto

## Como Rodar

### 1. Instalar dependencias

```powershell
python -m pip install -e ".[dev]"
```

### 2. Subir o agente remoto A2A

Na raiz do projeto:

```powershell
uvicorn src.remote_a2a.study_explainer.agent:app --host localhost --port 8001
```

Isso disponibiliza o agent card em:

```text
http://localhost:8001/.well-known/agent-card.json
```

### 3. Configurar o agente ADK

Crie `src/agent/.env` com base em `src/agent/.env.example`.

### 4. Rodar o agente consumidor

Entre na pasta `src/` e rode:

```powershell
cd src
adk web --no-reload
```

ou:

```powershell
cd src
adk run agent
```

## Fluxo Esperado

### Perguntas curtas

Perguntas como "o que e dependency inversion?" podem ser atendidas pela tool local.

### Perguntas aprofundadas

Pedidos como "explique melhor dependency inversion e como praticar" devem ser delegados ao agente remoto A2A.

## Como Ler O Codigo

### 1. Dominio primeiro

Leia `src/core/study_explainer.py`.

### 2. Depois o executor

Leia `StudyConceptAgentExecutor` em `src/remote_a2a/study_explainer/agent.py`.

Ele e o ponto em que o protocolo A2A chama a logica real do agente.

### 3. Por fim o consumidor

Veja `src/agent/agent.py` para entender como o `RemoteA2aAgent` entra como subagente do ADK.
