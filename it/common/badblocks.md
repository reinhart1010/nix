---
layout: page
title: common/badblocks (italiano)
description: "Cerca blocchi corrotti in un dispositivo."
content_hash: 55fb67af8fe03c1346ccdad424258012506ef6d4
related_topics:
  - title: English version
    url: /en/common/badblocks.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/badblocks.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/badblocks.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># badblocks

Cerca blocchi corrotti in un dispositivo.
Alcuni utilizzi di badblocks possono avere esiti non reversibili, come perdita dei dati o anche della tabella delle partizioni di un disco.
Maggiori informazioni: <https://manned.org/badblocks>.

- Cerca blocchi corrotti in un disco utilizzando un test non distruttivo in sola lettura:

`sudo badblocks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>

- Cerca blocchi corrotti in un disco non montato con un test non distruttivo in lettura e scrittura:

`sudo badblocks -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>

- Cerca blocchi corrotti in un disco non montato con un test distruttivo in scrittura:

`sudo badblocks -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>
