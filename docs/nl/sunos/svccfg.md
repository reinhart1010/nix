---
layout: page
title: sunos/svccfg (Nederlands)
description: "Importeer, exporteer, en wijzig service configurations."
content_hash: a9333cc67cc799a771f0cbd723ca85007b9966a0
related_topics:
  - title: English version
    url: /en/sunos/svccfg.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/svccfg.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># svccfg

Importeer, exporteer, en wijzig service configurations.
Meer informatie: <https://www.unix.com/man-page/linux/1m/svccfg>.

- Validatie van een configuratie bestand:

`svccfg validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smf.xml</span>

- Exporteer de configuratie van een service naar een bestand:

`svccfg export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servicename</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smf.xml</span>

- Update de service configuratie aan de hand van een bestand:

`svccfg import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smf.xml</span>
