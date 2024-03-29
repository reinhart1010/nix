---
layout: page
title: common/python (português (Brasil))
description: "Interpretador da linguagem Python."
content_hash: 210c6049d6965c7d60b26a0409d6bea417ba1359
last_modified_at: 2023-12-21
related_topics:
  - title: English version
    url: /en/common/python.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/python.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/python.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/python.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/python.html
    icon: bi bi-globe
tldri18n_status: 2
---
# python

Interpretador da linguagem Python.
Mais informações: <https://www.python.org>.

- Inicia o REPL (shell interativo):

`python`

- Executa um arquivo Python específico:

`python `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.py</span>

- Executa um arquivo Python específico e inicia um REPL:

`python -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.py</span>

- Executa uma expressão em Python:

`python -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expressão</span>`"`

- Roda o script do módulo de biblioteca especificado:

`python -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modulo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumentos</span>

- Instala um pacote usando `pip`:

`python -m pip install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Depura interativamente um script de Python:

`python -m pdb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.py</span>

- Inicia o servidor HTTP integrado na porta 8000 no diretório atual:

`python -m http.server`
