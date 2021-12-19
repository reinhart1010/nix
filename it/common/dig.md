---
layout: page
title: common/dig (italiano)
description: "Utilità di lookup DNS."
content_hash: 8e4567fd27f8e8d6921cb54f98dac9b123fed41a
related_topics:
  - title: English version
    url: /en/common/dig.html
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
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dig.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dig

Utilità di lookup DNS.
Maggiori informazioni: <https://manpages.debian.org/dnsutils/dig.1.html>.

- Mostra gli IP associati ad un hostname (record A):

`dig +short `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">esempio.com</span>

- Mostra i mail server associati ad uno specifico dominio (record MX):

`dig +short `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">esempio.com</span>` MX`

- Richiedi tutti i tipi di record per un dato dominio:

`dig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">esempio.com</span>` ANY`

- Specifica un server DNS alternativo a cui fare richiesta:

`dig @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">esempio.com</span>

- Esegui un lookup DNS inverso su di un indirizzo IP (record PTR):

`dig -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>

- Trova i nameserver autoritativi per la zona e mostra i record SOA:

`dig +nssearch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">esempio.com</span>

- Esegui richieste iterative e mostra l'intero percorso per risolvere il dominio:

`dig +trace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">esempio.com</span>
