# Learning How To Code Better

Projeto educacional para estudar:

- Clean Code
- SOLID
- Python com foco em legibilidade e manutenção
- Google ADK para construção de agentes
- A2A como próxima etapa de evolução
- AgentExecutor como ponte entre protocolo e lógica do agente remoto

## Objetivo

Este repositório foi estruturado para ensinar como escrever código mais limpo, claro e sustentável. A ideia não é apenas "fazer funcionar", mas entender como organizar responsabilidades, escolher bons nomes e reduzir acoplamento desde o começo.

O projeto evolui em duas etapas:

1. Fundamentos de Clean Code e SOLID com exemplos pequenos.
2. Aplicação desses princípios em um agente construído com Google ADK.

## Estrutura

- `docs/`: material de estudo resumido.
- `examples/bad_vs_good/`: comparações entre código ruim e código refatorado.
- `src/core/`: regras de domínio e serviços puros.
- `src/tools/`: tools usadas pelo agente.
- `src/agent/`: agente ADK principal.
- `tests/`: testes dos serviços e exemplos centrais.

## Trilha De Aprendizado

### 1. Clean Code

Leia primeiro:

- `docs/clean-code.md`
- `examples/bad_vs_good/meaningful_names_bad.py`
- `examples/bad_vs_good/meaningful_names_good.py`
- `examples/bad_vs_good/single_responsibility_bad.py`
- `examples/bad_vs_good/single_responsibility_good.py`

### 2. SOLID

Depois avance para:

- `docs/solid.md`
- `examples/bad_vs_good/dependency_inversion_bad.py`
- `examples/bad_vs_good/dependency_inversion_good.py`

### 3. Aplicando Em Um Agente

Por fim, veja como os mesmos princípios aparecem no agente:

- `src/core/study_catalog.py`
- `src/tools/study_lookup.py`
- `src/agent/agent.py`

### 4. Fase 2: A2A

Depois avance para:

- `src/core/study_explainer.py`
- `src/remote_a2a/study_explainer/agent.py`
- `docs/a2a-quickstart.md`

## Como Rodar

### 1. Criar ambiente virtual

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Instalar dependências

```powershell
pip install -e .[dev]
```

### 3. Configurar variáveis do agente

Use o arquivo `src/agent/.env.example` como referência para criar `src/agent/.env`.

### 4. Executar testes

```powershell
python -m pytest
```

### 5. Rodar o agente ADK

Execute a partir da pasta `src/`:

```powershell
cd src
adk run agent
```

Para abrir a interface web do ADK:

```powershell
cd src
adk web --no-reload
```

## Rodando A Fase 2

Suba primeiro o agente remoto A2A:

```powershell
uvicorn src.remote_a2a.study_explainer.agent:app --host localhost --port 8001
```

Depois, em outro terminal:

```powershell
cd src
adk web --no-reload
```

Guia detalhado:

- `docs/a2a-quickstart.md`

## Próxima Etapa

A base da integração A2A foi implementada no código. O planejamento de evolução continua em `docs/a2a-roadmap.md`.