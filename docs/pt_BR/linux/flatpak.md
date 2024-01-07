---
layout: page
title: linux/flatpak (português (Brasil))
description: "Construa, instale e execute aplicações e plataformas flatpak."
content_hash: a54599bb616928351067421564d83fd4ca9f4e87
last_modified_at: 2024-01-07
related_topics:
  - title: English version
    url: /en/linux/flatpak.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/flatpak.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/flatpak.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/flatpak.html
    icon: bi bi-globe
tldri18n_status: 2
---
# flatpak

Construa, instale e execute aplicações e plataformas flatpak.
Mais informações: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak>.

- Executa uma aplicação instalada:

`flatpak run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Instala uma aplicação de uma fonte remota:

`flatpak install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remoto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Lista todas as aplicações e plataformas instaladas:

`flatpak list`

- Atualiza todas as aplicações e plataformas instaladas:

`flatpak update`

- Adiciona uma fonte remota:

`flatpak remote-add --if-not-exists `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_remoto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_remoto</span>

- Remove uma aplicação instalada:

`flatpak remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Remove todos as aplicações não usadas:

`flatpak remove --unused`

- Mostra informações sobre uma aplicação instalada:

`flatpak info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>
