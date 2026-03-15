# Clean Code Em Python

## Ideia Central

Código limpo é código fácil de entender, mudar e testar. Quando alguém lê uma função, ela deve comunicar intenção rapidamente, sem exigir esforço desnecessário para decifrar nomes vagos, regras escondidas ou responsabilidades misturadas.

## Conceitos Principais

### 1. Nomes Significativos

Prefira nomes que mostrem intenção.

- Ruim: `x`, `data`, `handle()`
- Melhor: `student_name`, `study_topics`, `build_feedback()`

Pergunta útil: "alguém que abriu este arquivo agora entende o que isso representa?"

### 2. Funções Pequenas

Uma função pequena costuma:

- fazer uma coisa só,
- ter poucos argumentos,
- ser fácil de testar,
- ter nome coerente com sua responsabilidade.

Se a função precisa explicar várias etapas não relacionadas, provavelmente ela merece ser quebrada.

### 3. Uma Responsabilidade Por Unidade

Se uma função carrega dados, valida, formata e salva tudo ao mesmo tempo, ela ficou grande demais. Separar essas etapas reduz acoplamento e torna mudanças futuras menos arriscadas.

### 4. Comentários São Apoio, Não Muleta

O melhor comentário é um código claro. Comentários são úteis quando:

- há uma decisão de negócio pouco óbvia,
- existe uma restrição externa,
- um detalhe técnico não é intuitivo.

Se o comentário só traduz o que o código já deveria expressar, vale renomear ou refatorar.

### 5. Tratamento De Erros Claro

Erros precisam ser compreensíveis e previsíveis. Em vez de mensagens genéricas, retorne contexto suficiente para facilitar depuração e uso da API.

### 6. Evite Duplicação

Duplicação espalha regra de negócio e aumenta chance de inconsistência. Extraia uma função ou serviço quando uma ideia importante aparece repetidamente.

## Como Este Projeto Aplica Isso

- `src/core/study_catalog.py` separa dados, busca e formatação.
- `src/tools/study_lookup.py` expõe uma tool simples para o agente sem misturar regra de negócio com a camada do ADK.
- `src/agent/agent.py` foca em orquestração, não na lógica do domínio.

## Sugestão De Estudo

1. Leia os arquivos em `examples/bad_vs_good/`.
2. Compare o nome das funções e a quantidade de responsabilidades em cada versão.
3. Rode os testes para ver como código mais limpo tende a ser mais fácil de validar.
