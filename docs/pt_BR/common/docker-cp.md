---
layout: page
title: common/docker-cp (português (Brasil))
description: "Copia arquivos ou diretórios entre filesystems do host e container."
content_hash: 970db8daf6e046fd63a9a5887b937a0fcaf04b4d
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/docker-cp.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-cp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-cp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-cp.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-cp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker cp

Copia arquivos ou diretórios entre filesystems do host e container.
Mais informações: <https://docs.docker.com/engine/reference/commandline/cp>.

- Copia um arquivo ou diretório de um host para um container:

`docker cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/arquivo_ou_diretório_do_host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_container</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/arquivo_ou_diretório_do_container</span>

- Copia um arquivo ou diretório de um container para o host:

`docker cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_container</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/arquivo_ou_diretório_do_container</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/arquivo_ou_diretório_do_host</span>

- Copia um diretório de um host para um container, seguindo o link simbólico (copia os arquivos linkados diretamente e não o link simbólico):

`docker cp --follow-link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/arquivo_ou_diretório_linkado_do_host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_container</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/arquivo_ou_diretório_do_container</span>
