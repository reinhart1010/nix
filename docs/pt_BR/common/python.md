---
layout: page
title: common/python (português (Brasil))
description: "O interpretador de linguagem Python."
content_hash: 01a1d41b59ca1f305af95b26b107f28aba291896
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

O interpretador de linguagem Python.
Mais informações: <https://www.python.org>.

- Inicia o REPL (shell interativo):

`python`

- Executa o script do arquivo Python alvo:

`python `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.py</span>

- Executa o script como parte do shell interativo:

`python -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.py</span>

- Executa uma expressão em Python:

`python -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expressão</span>`"`

- Roda um módulo de biblioteca como um script (declara o fim da lista de opções):

`python -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modulo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumentos</span>

- Instala um pacote usando pip:

`python -m pip install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Depura interativamente um script de Python:

`python -m pdb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.py</span>
