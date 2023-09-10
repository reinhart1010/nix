---
layout: page
title: common/calibre-server (italiano)
description: "Un'applicazione server che può essere usata per distribuire e-book in una rete."
content_hash: fb463eb118f02b295560508eabef5a7f68a967ea
last_modified_at: 2023-09-10
related_topics:
  - title: English version
    url: /en/common/calibre-server.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/calibre-server.html
    icon: bi bi-globe
---
# calibre-server

Un'applicazione server che può essere usata per distribuire e-book in una rete.
Gli e-book devono prima essere importati nella libreria usando la GUI o calibredb.
Parte del manager di e-book Calibre.
Maggiori informazioni: <https://manual.calibre-ebook.com/generated/en/calibre-server.html>.

- Avvia un server per distribuire e-book. Accesso a <http://localhost:8080>:

`calibre-server`

- Avvia il server su una specifica porta. Accesso a <http://localhost:porta>:

`calibre-server --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta</span>

- Proteggi il server con username e password:

`calibre-server --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>
