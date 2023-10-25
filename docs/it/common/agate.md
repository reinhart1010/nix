---
layout: page
title: common/agate (italiano)
description: "Un semplice server per il protocollo di rete Gemini."
content_hash: 0c79d6efddf0d1e742c4e8bb9599e252330377e7
last_modified_at: 2023-10-25
related_topics:
  - title: English version
    url: /en/common/agate.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/agate.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/agate.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/agate.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/agate.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/agate.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># agate

Un semplice server per il protocollo di rete Gemini.
Maggiori informazioni: <https://github.com/mbrubeck/agate>.

- Esegui e genera una chiave privata e un certificato:

`agate --content `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/contenuto</span>` --addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[::]:1965</span>` --addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.0.0.0:1965</span>` --hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">esempio.it</span>` --lang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">it-IT</span>

- Avvia server:

`agate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Visualizza la guida:

`agate -h`
