---
layout: page
title: common/darkhttpd (italiano)
description: "Web server Darkhttpd."
content_hash: 18c488b3bd41911b7ad1f942e46a720235113de5
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/darkhttpd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/darkhttpd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/darkhttpd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# darkhttpd

Web server Darkhttpd.
Maggiori informazioni: <https://unix4lyfe.org/darkhttpd>.

- Avvia il server utilizzando la directory specificata come document root:

`darkhttpd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/docroot</span>

- Avvia il server su una specifica porta (8080 di default per utenti non root):

`darkhttpd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/docroot</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta</span>

- Ascolta solo su uno specifico indirizzo IP (di default, il server ascolta su tutte le interfacce):

`darkhttpd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/docroot</span>` --addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indirizzo_ip</span>
