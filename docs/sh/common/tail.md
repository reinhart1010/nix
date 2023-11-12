---
layout: page
title: common/tail (sh)
description: "Prikazuje krajnji deo datoteke."
content_hash: 33480f5607343ab7e7e72979fbc90909a93dda42
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/tail.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/tail.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tail.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># tail

Prikazuje krajnji deo datoteke.
Više informacija: <https://www.gnu.org/software/coreutils/tail>.

- Prikaži poslednjih 'broj' linija u datoteci:

`tail -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">broj</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka</span>

- Prikaži celu datoteku od linije 'broj':

`tail -n +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">broj</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka</span>

- Prikaži poslednjih 'broj' bajtova u datoteci:

`tail -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">broj</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka</span>

- Čitaj datoteku sve do `Ctrl + C`:

`tail -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka</span>

- Čitaj datoteku sve do `Ctrl + C`, čak i kad je datoteka rotirana:

`tail -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datoteka</span>
