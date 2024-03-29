---
layout: page
title: common/pip (português (Brasil))
description: "Gerenciador de pacotes para Python."
content_hash: 8cb83fc929bbecb597952486b654cdb88b78e701
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/pip.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/pip.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/pip.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/pip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pip

Gerenciador de pacotes para Python.
Alguns sub-comandos, como `pip install` possuem sua própria documentação.
Mais informações: <https://pip.pypa.io>.

- Instala um pacote (veja `pip install` para mais exemplos de instalação):

`pip install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacote</span>

- Instala um pacote no diretório do usuário em vez do local padrão do sistema:

`pip install --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacote</span>

- Atualiza um pacote:

`pip install --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacote</span>

- Desinstala um pacote:

`pip uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacote</span>

- Salva os pacotes instalados em um arquivo:

`pip freeze > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requirements.txt</span>

- Mostra informações sobre um pacote instalado:

`pip show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacote</span>

- Instala pacotes a partir de um arquivo:

`pip install --requirement `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requirements.txt</span>
