---
layout: page
title: linux/distrobox-upgrade (português (Brasil))
description: "Atualizar um ou vários contêineres distrobox."
content_hash: ee9ff830dd07cda2a512665c334a0ade61742718
last_modified_at: 2023-09-08
related_topics:
  - title: English version
    url: /en/linux/distrobox-upgrade.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># distrobox-upgrade

Atualizar um ou vários contêineres distrobox.
Subcomando de `distrobox`. Veja também: `tldr distrobox`.
Mais informações: <https://distrobox.privatedns.org/usage/distrobox-upgrade.html>.

- Atualizar um contêiner usando o gerenciador de pacotes nativo do contêiner:

`distrobox-upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>

- Atualizar todos os contêineres usando os gerenciadores de pacotes nativos dos contêineres:

`distrobox-upgrade --all`

- Atualizar contêineres específicos via o gerenciador de pacotes nativo do contêiner:

`distrobox-upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contêiner1 contêiner2 ...</span>
