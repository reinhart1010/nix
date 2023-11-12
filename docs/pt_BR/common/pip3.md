---
layout: page
title: common/pip3 (português (Brasil))
description: "Gerenciador de pacotes Python."
content_hash: 919415618d02413402dbf6ca57b6dbcd0bee3b82
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/pip3.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/pip3.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/pip3.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pip3

Gerenciador de pacotes Python.
Mais informações: <https://pip.pypa.io>.

- Instala um pacote:

`pip3 install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacote</span>

- Instala uma versão específica de um pacote:

`pip3 install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacote</span>`==`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versão_pacote</span>

- Atualiza um pacote:

`pip3 install --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacote</span>

- Desinstala um pacote:

`pip3 uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacote</span>

- Salva a lista de pacotes instalados em um arquivo:

`pip3 freeze > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requirements.txt</span>

- Instala pacotes salvos em um arquivo:

`pip3 install --requirement `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requirements.txt</span>

- Mostra informações sobre um pacote instalado:

`pip3 show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacote</span>
