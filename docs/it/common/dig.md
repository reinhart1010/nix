---
layout: page
title: common/dig (italiano)
description: "Utilità di lookup DNS."
content_hash: c9ffd9a47726e2debdc1475cf755fd31e33e30c6
last_modified_at: 2023-12-20
related_topics:
  - title: English version
    url: /en/common/dig.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/dig.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/dig.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dig.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/dig.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/dig.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dig

Utilità di lookup DNS.
Maggiori informazioni: <https://manned.org/dig>.

- Mostra gli IP associati ad un hostname (record A):

`dig +short `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">esempio.com</span>

- Mostra i mail server associati ad uno specifico dominio (record MX):

`dig +short `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">esempio.com</span>` MX`

- Specifica un server DNS alternativo a cui fare richiesta:

`dig @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">esempio.com</span>

- Esegui un lookup DNS inverso su di un indirizzo IP (record PTR):

`dig -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>

- Trova i nameserver autoritativi per la zona e mostra i record SOA:

`dig +nssearch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">esempio.com</span>

- Esegui richieste iterative e mostra l'intero percorso per risolvere il dominio:

`dig +trace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">esempio.com</span>
