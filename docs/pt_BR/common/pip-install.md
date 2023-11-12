---
layout: page
title: common/pip-install (português (Brasil))
description: "Instala pacotes Python."
content_hash: d78d91dc5c7f9826b8b1a3ae71ae06688e98f467
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/pip-install.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/pip-install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pip install

Instala pacotes Python.
Mais informações: <https://pip.pypa.io>.

- Instala um pacote:

`pip install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacote</span>

- Instala uma versão específica de um pacote:

`pip install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacote</span>`==`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versão_do_pacote</span>

- Instala pacotes listados em um arquivo:

`pip install --requirement `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requirements.txt</span>

- Instala pacotes a partir de uma URL ou arquivo local (.tar.gz | .whl):

`pip install --find-links `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|caminho/do/arquivo</span>

- Instala o pacote local no diretório atual no modo de desenvolvimento (editável):

`pip install --editable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>
