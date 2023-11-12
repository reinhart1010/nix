---
layout: page
title: common/badblocks (italiano)
description: "Cerca blocchi corrotti in un dispositivo."
content_hash: 55fb67af8fe03c1346ccdad424258012506ef6d4
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/badblocks.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/badblocks.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

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
