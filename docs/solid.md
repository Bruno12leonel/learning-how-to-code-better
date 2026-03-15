# SOLID Em Python

## Objetivo

SOLID é um conjunto de princípios de design orientado a objetos que ajuda a produzir código mais flexível, legível e fácil de manter.

## Os 5 Princípios

### SRP: Single Responsibility Principle

Cada módulo, classe ou função deve ter um motivo principal para mudar.

Sinal de problema:

- a mesma função consulta dados,
- decide regras,
- formata resposta,
- grava em arquivo.

Aplicação neste projeto:

- `src/core/study_catalog.py` cuida do domínio.
- `src/tools/study_lookup.py` cuida da integração com a tool.

### OCP: Open/Closed Principle

Seu código deve estar aberto para extensão, mas fechado para modificação frequente de partes estáveis.

Exemplo prático:

Se você quiser adicionar novos tópicos de estudo, deve poder fazer isso adicionando dados ou uma nova implementação de provedor, sem reescrever o serviço inteiro.

### LSP: Liskov Substitution Principle

Uma implementação concreta deve poder substituir a abstração esperada sem quebrar comportamento.

Neste projeto, um provedor em memória pode ser trocado por um provedor vindo de arquivo ou banco, desde que mantenha o mesmo contrato.

### ISP: Interface Segregation Principle

Prefira contratos pequenos e focados. Quem consome uma abstração não deve depender de métodos que não usa.

Aplicação:

- `StudyContentProvider` define somente o que o serviço realmente precisa para buscar tópicos.

### DIP: Dependency Inversion Principle

Módulos de alto nível não devem depender diretamente de detalhes concretos, mas de abstrações.

Aplicação:

- `StudyCatalogService` depende do protocolo `StudyContentProvider`.
- A implementação concreta é injetada por fora.

## Como Estudar Aqui

1. Veja `examples/bad_vs_good/dependency_inversion_bad.py`.
2. Compare com `examples/bad_vs_good/dependency_inversion_good.py`.
3. Depois leia `src/core/contracts.py` e `src/core/study_catalog.py`.

## Regra Prática

Antes de criar uma classe nova, pergunte:

- ela tem uma responsabilidade clara?
- ela depende de algo muito concreto?
- eu conseguiria testar isso sem infraestrutura real?

Se a resposta for "não", o design provavelmente pode melhorar.
