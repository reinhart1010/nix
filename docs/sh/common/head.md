---
layout: page
title: common/head (sh)
description: "Prikazuje prvi deo datoteka."
content_hash: ac33a75f7761783c534c55b77efb041b80b7a019
last_modified_at: 2023-11-06
related_topics:
  - title: Deutsch version
    url: /de/common/head.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/head.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/head.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/head.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/head.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/head.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># head

Prikazuje prvi deo datoteka.
Više informacija: <https://manned.org/head.1p>.

- Prikaži prvih nekoliko linija datoteke:

`head -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">broj_linija</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">naziv_datoteke</span>

- Prikaži prvih nekoliko bajtova datoteke:

`head -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">veličina_u_bajtovima</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">naziv_datoteke</span>

- Prikaži sve osim nekoliko poslednjih linija datoteke:

`head -n -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">broj_linija</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">naziv_datoteke</span>

- Prikaži sve osim nekoliko poslednjih bajtova datoteke:

`head -c -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">veličina_u_bajtovima</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">naziv_datoteke</span>
