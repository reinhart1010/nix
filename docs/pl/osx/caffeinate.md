---
layout: page
title: osx/caffeinate (polski)
description: "Nie pozwól aby macOS się uśpił."
content_hash: 19c1c720b3b06955b0b2626278c76cf5c4e73baf
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/osx/caffeinate.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/caffeinate.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/caffeinate.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/caffeinate.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/caffeinate.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/caffeinate.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/caffeinate.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># caffeinate

Nie pozwól aby macOS się uśpił.
Więcej informacji: <https://ss64.com/osx/caffeinate.html>.

- Nie usypiaj przez 1 godzinę (3600 sekund):

`caffeinate -u -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>

- Nie usypiaj dopóki komenda nie zostanie zakończona:

`caffeinate -s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- Nie usypiaj dopóki nie przerwiesz naciskając `Ctrl - C`:

`caffeinate -i`

- Nie usypiaj dysku twardego dopóki nie przerwiesz naciskając `Ctrl + C`:

`caffeinate -m`
