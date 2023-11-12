---
layout: page
title: common/dokku (italiano)
description: "Mini-Heroku basato su Docker (PaaS, Platform As A Service)."
content_hash: 7295bfdd079a1b2241dc3bab3864a4ebc5c46a46
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/dokku.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dokku.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/dokku.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dokku

Mini-Heroku basato su Docker (PaaS, Platform As A Service).
Distribuisci facilmente molteplici app sul tuo server in diversi linguaggi utilizzando un singolo comando `git-push`.
Maggiori informazioni: <https://github.com/dokku/dokku>.

- Elenca app in esecuzione:

`dokku apps`

- Crea un'app:

`dokku apps:create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_app</span>

- Rimuovi un'app:

`dokku apps:destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_app</span>

- Installa un plugin:

`dokku plugin:install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_completo_repo</span>

- Collega un database ad un'app:

`dokku `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">db</span>`:link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_db</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_app</span>
