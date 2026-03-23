# Machine Learning - Atividade 5 | PNL (Processamento de Linguagem Natural)

Repositório da 3ª Etapa da Sprint-02 (AC-2) — Disciplina de Machine Learning 2026.

## Descrição

Atividades práticas de PNL utilizando Python, NLTK e Scikit-learn. O objetivo é explorar técnicas fundamentais de processamento de linguagem natural como tokenização, remoção de stopwords, vetorização e classificação de intenções.

## Dependências

```bash
pip install nltk scikit-learn
```

## Atividades

### Atividade 1 — Tokenização (`atv_nlp_01.py`)
Tokeniza uma frase usando NLTK e conta a quantidade de tokens.

**Resultado:**
```
['Machine', 'Learning', 'é', 'uma', 'das', 'áreas', 'mais', 'importantes', 'da', 'Inteligência', 'Artificial', '.']
A quantidade de tokens na mensagem é: 12
```

---

### Atividade 2 — Pipeline PNL (`atv_nlp_02.py`)
Pipeline completo com 3 etapas:
- Etapa 1: Normalização de texto (minúsculo + remoção de pontuação)
- Etapa 2: Filtro de stopwords em português
- Etapa 3: Detector de urgência por palavras-chave

**Resultado:**
```
--- Exercício 1: Normalizador ---
Original: ERRO Crítico no Servidor!!! Código: #404... favor verificar AGORA.
Limpo:    erro crítico no servidor código 404 favor verificar agora

--- Exercício 2: Filtro de Relevância ---
Frase:  O meu boleto ainda não chegou no meu e-mail
Tokens: ['boleto', 'ainda', 'chegou']
Frase:  Gostaria de falar com um atendente humano por favor
Tokens: ['gostaria', 'falar', 'atendente', 'humano', 'favor']

--- Exercício 3: Detector de Urgência ---
[ALTA PRIORIDADE] Mensagem: Olá, estou com um problema urgente, meu sistema está parado!
[NORMAL] Mensagem: Bom dia, gostaria de saber o preço do plano premium.
[ALTA PRIORIDADE] Mensagem: Erro fatal na integração, socorro!!!
```

---

### Atividade 3 — Limpeza de Texto (`atv_nlp_03.py`)
Remove stopwords de uma frase em português, mantendo apenas palavras relevantes.

**Resultado:**
```
['quero', 'aprender', 'Machine', 'Learning', 'criar', 'chatbots', 'inteligentes']
```

---

### Atividade 4 — Vetorização de Texto (`atv_nlp_04.py`)
Converte frases em matriz numérica usando Bag of Words (CountVectorizer).

**Resultado:**
```
['cancelar' 'comprar' 'eu' 'horário' 'qual' 'quero']
[[0 1 1 0 0 1]
 [1 0 1 0 0 1]
 [0 0 0 1 1 0]]
```

---

### Atividade 5 — Contador de Palavras (`atv_pnl_05.py`)
Divide um texto em palavras e conta a quantidade total.

**Resultado:**
```
Número de palavras: 7
```

---

### Atividade 6 — Frequência de Palavras (`atv_pnl_06.py`)
Calcula a frequência de cada palavra em um texto usando `Counter`.

**Resultado:**
```
Counter({'chatbot': 3, 'inteligência': 1, 'artificial': 1, 'aprendizado': 1})
```

---

### Atividade 7 — Classificador de Intenção (`atv_pnl_07.py`)
Treina um modelo Naive Bayes para classificar intenções de mensagens (comprar, cancelar, horario).

**Como rodar:**
```bash
python atv_pnl_07.py
```

**Resultado esperado:**
```
Digite sua mensagem: quero saber horário
Intenção detectada: horario
```

---

## Como executar

```bash
python atv_nlp_01.py
python atv_nlp_02.py
python atv_nlp_03.py
python atv_nlp_04.py
python atv_pnl_05.py
python atv_pnl_06.py
python atv_pnl_07.py  # requer input do usuário
```

## Referências

- [Repositório do Professor](https://github.com/PROFSANTARELLI/CDC-MACHINE-LEARNING-2026)
- [Documentação NLTK](https://www.nltk.org/)
- [Documentação Scikit-learn](https://scikit-learn.org/)
