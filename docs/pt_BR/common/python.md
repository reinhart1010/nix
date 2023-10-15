---
layout: page
title: common/python (português (Brasil))
description: "Interpretador da linguagem Python."
content_hash: bdaea74b09948804eae62951c2bcaad198a8cf5a
last_modified_at: 2023-10-15
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
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/python.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># python

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

`python -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.py</span>

- Inicia o servidor HTTP integrado na porta 8000 no diretório atual:

`python -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http.server</span>
