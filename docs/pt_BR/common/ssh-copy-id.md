---
layout: page
title: common/ssh-copy-id (português (Brasil))
description: "Instala a sua chave pública no arquivo authorized_keys de uma máquina remota."
content_hash: 858401b276ea8772ccf87b8c6fba24e36eb428cc
last_modified_at: 2024-10-17
related_topics:
  - title: Deutsch version
    url: /de/common/ssh-copy-id.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ssh-copy-id.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ssh-copy-id.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ssh-copy-id

Instala a sua chave pública no arquivo authorized_keys de uma máquina remota.
Mais informações: <https://manned.org/ssh-copy-id>.

- Copia suas chaves para a máquina remota:

`ssh-copy-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_de_usuário</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">máquina_remota</span>

- Copia a chave pública fornecida para a máquina remota:

`ssh-copy-id -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/certificado</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_de_usuário</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">maquina_remota</span>

- Copia a chave pública fornecida para a máquina remota usando uma porta específica:

`ssh-copy-id -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/certificado</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_de_usuário</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">maquina_remota</span>
