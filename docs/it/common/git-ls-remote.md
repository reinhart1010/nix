---
layout: page
title: common/git-ls-remote (italiano)
description: "Elenca i riferimenti in un repository remoto dato un nome o un URL."
content_hash: 2f5c130d7339e9211c48219879ae22d977e30d0b
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-ls-remote.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-ls-remote.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-ls-remote.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git ls-remote

Elenca i riferimenti in un repository remoto dato un nome o un URL.
Qualora né nome né URL siano specificati, il ramo predefinito è upstream - se configurato - oppure origin.
Maggiori informazioni: <https://git-scm.com/docs/git-ls-remote>.

- Mostra tutti i riferimenti nel repository remoto predefinito:

`git ls-remote`

- Mostra solo i riferimenti HEAD nel repository remoto predefinito:

`git ls-remote --heads`

- Mostra solo i riferimenti a tag nel repository remoto predefinito:

`git ls-remote --tags`

- Mostra tutti i riferimenti da un repository remoto dato un nome o URL:

`git ls-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_repository</span>

- Filtra i riferimenti da un repository remoto rispetto a un dato criterio:

`git ls-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_repository</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">criterio</span>`"`
