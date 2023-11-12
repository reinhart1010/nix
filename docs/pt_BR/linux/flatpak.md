---
layout: page
title: linux/flatpak (português (Brasil))
description: "Construa, instale e execute aplicações e plataformas flatpak."
content_hash: ee75ed15b3c5717f7b7cfb8509f0ca13b55871fe
last_modified_at: 2023-11-12
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

- Executar uma aplicação instalada:

`flatpak run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Instalar uma aplicação de uma fonte remota:

`flatpak install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remoto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Listar todas as aplicações e plataformas instaladas:

`flatpak list`

- Atualizar todas as aplicações e plataformas instaladas:

`flatpak update`

- Adicionar uma fonte remota:

`flatpak remote-add --if-not-exists `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_remoto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_remoto</span>

- Listar todas fontes remotas configuradas:

`flatpak remote-list`

- Remover uma aplicação instalada:

`flatpak remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Mostrar informações sobre uma aplicação instalada:

`flatpak info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>
