---
layout: page
title: common/git-instaweb (italiano)
description: "Helper per avviare un server gitweb."
content_hash: 7259c81e551248f218bb2b31435f12ccfd8d056e
related_topics:
  - title: English version
    url: /en/common/git-instaweb.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-instaweb.html
    icon: bi bi-globe
---
# git instaweb

Helper per avviare un server gitweb.
Maggiori informazioni: <https://git-scm.com/docs/git-instaweb>.

- Avvia un server gitweb dal repository corrente:

`git instaweb --start`

- Resta in ascolto solo su localhost:

`git instaweb --start --local`

- Resta in ascolto su una porta specifica:

`git instaweb --start --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>

- Usa un http daemon specifico:

`git instaweb --start --httpd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lighttpd|apache2|mongoose|plackup|webrick</span>

- Avvia automaticamente anche un web browser:

`git instaweb --start --browser`

- Interrompi il server gitweb in esecuzione:

`git instaweb --stop`

- Riavvia il server gitweb in esecuzione:

`git instaweb --restart`
