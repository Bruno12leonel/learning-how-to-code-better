# Roadmap Da Fase A2A

## Objetivo

Adicionar A2A somente depois que o agente único estiver estável, compreensível e bem testado.

## O Que Já Existe

- Um domínio simples de estudo em `src/core/`
- Uma tool local em `src/tools/`
- Um agente ADK principal em `src/agent/`

## O Que Entrará Na Fase 2

### Cenário Sugerido

O agente principal continuará recebendo a pergunta do usuário, mas poderá delegar uma tarefa específica para um agente remoto especializado.

Exemplo:

- agente principal: entende a intenção do usuário,
- agente remoto: explica um conceito de Clean Code ou SOLID com mais profundidade.

### Objetivos Técnicos

1. Expor um agente via A2A.
2. Fazer o agente principal consumir esse agente remoto.
3. Manter o caso de uso pequeno e observável.

### Papel Do AgentExecutor

Na fase 2, o foco nao sera apenas "chamar outro agente", mas entender a camada de execucao do protocolo:

- `AgentCard`: descreve capacidades do agente remoto.
- `AgentExecutor`: implementa o fluxo principal de processamento.
- `execute()`: recebe a requisicao e produz eventos ou respostas.
- `cancel()`: trata cancelamento do trabalho em andamento.

A ideia educacional e estudar o `AgentExecutor` como o ponto onde a orquestracao do agente remoto acontece, mantendo a logica de dominio separada dele.

### Dependencia Esperada

Quando essa fase começar, a instalacao deve evoluir de:

- `google-adk`

para:

- `google-adk[a2a]`

## Limites Intencionais

Para evitar complexidade cedo demais, esta fase não deve incluir:

- memória longa,
- múltiplos agentes paralelos,
- planejamento complexo,
- integração com banco de dados.

## Checklist Para Começar A Fase 2

- o agente local já responde bem com tools locais,
- os testes do domínio estão estáveis,
- a separação entre domínio, tool e orquestração está clara,
- o fluxo principal já está fácil de explicar e depurar.
