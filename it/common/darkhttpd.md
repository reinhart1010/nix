---
layout: page
title: common/darkhttpd (italiano)
description: "Web server Darkhttpd."
content_hash: ead99ecf0d54726555fc6172f5f70bb68b2b93b6
related_topics:
  - title: English version
    url: /en/common/darkhttpd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/darkhttpd.html
    icon: bi bi-globe
---
# darkhttpd

Web server Darkhttpd.
Maggiori informazioni: <https://unix4lyfe.org/darkhttpd>.

- Avvia il server utilizzando la directory specificata come document root:

`darkhttpd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/docroot</span>

- Avvia il server su una specifica porta (8080 di default per utenti non root):

`darkhttpd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/docroot</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta</span>

- Ascolta solo su uno specifico indirizzo IP (di default, il server ascolta su tutte le interfacce):

`darkhttpd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/docroot</span>` --addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indirizzo_ip</span>
