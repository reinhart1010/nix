---
layout: page
title: common/calibre-server (italiano)
description: "Un'applicazione server che può essere usata per distribuire e-book in una rete."
content_hash: bab034f0b55d622cda6127696ccff13fdf7dc4a9
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

- Avvia un server per distribuire e-book. Accesso a http://localhost:8080:

`calibre-server`

- Avvia il server su una specifica porta. Accesso a http://localhost:porta:

`calibre-server --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta</span>

- Proteggi il server con username e password:

`calibre-server --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>
