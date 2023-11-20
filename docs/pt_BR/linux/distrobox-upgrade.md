---
layout: page
title: linux/distrobox-upgrade (português (Brasil))
description: "Atualizar um ou vários contêineres distrobox."
content_hash: f36ca87dd491a3fb18967de5cf2024ea6bef3ab6
last_modified_at: 2023-11-20
related_topics:
  - title: English version
    url: /en/linux/distrobox-upgrade.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/distrobox-upgrade.html
    icon: bi bi-globe
tldri18n_status: 2
---
# distrobox-upgrade

Atualizar um ou vários contêineres distrobox.
Subcomando de `distrobox`. Veja também: `tldr distrobox`.
Mais informações: <https://distrobox.it/usage/distrobox-upgrade>.

- Atualizar um contêiner usando o gerenciador de pacotes nativo do contêiner:

`distrobox-upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>

- Atualizar todos os contêineres usando os gerenciadores de pacotes nativos dos contêineres:

`distrobox-upgrade --all`

- Atualizar contêineres específicos via o gerenciador de pacotes nativo do contêiner:

`distrobox-upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contêiner1 contêiner2 ...</span>
