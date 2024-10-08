---
layout: page
title: linux/pacaur (português (Brasil))
description: "Um utilitário para Arch Linux para construir e instalar pacotes a partir do Arch User Repository."
content_hash: 27180ae5b9724488cfe6281492b015e3b188c95a
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/linux/pacaur.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacaur

Um utilitário para Arch Linux para construir e instalar pacotes a partir do Arch User Repository.
Mais informações: <https://github.com/rmarquis/pacaur>.

- Sincroniza e atualiza todos os pacotes (inclui o AUR):

`pacaur -Syu`

- Sincroniza e atualiza apenas os pacotes do AUR:

`pacaur -Syua`

- Instala um novo pacote (inclui o AUR):

`pacaur -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Remove um pacote e suas dependências (inclui pacotes do AUR):

`pacaur -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Pesquisa o banco de dados de pacotes para uma palavra-chave (inclui o AUR):

`pacaur -Ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palavra-chave</span>

- Lista todos os pacotes atualmente instalados (inclui pacotes do AUR):

`pacaur -Qs`
