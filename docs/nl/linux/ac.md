---
layout: page
title: linux/ac (Nederlands)
description: "Toon statistieken over hoe lang gebruikers verbonden zijn geweest."
content_hash: 82adeaac2cb34c5d89da5a3131fff4936bae56d1
last_modified_at: 2024-08-13
related_topics:
  - title: català version
    url: /ca/linux/ac.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/ac.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ac.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/ac.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/ac.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ac.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/ac.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/ac.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/linux/ac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/ac.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ac.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ac

Toon statistieken over hoe lang gebruikers verbonden zijn geweest.
Meer informatie: <https://www.gnu.org/software/acct/manual/accounting.html#ac>.

- Toon hoe lang de huidige gebruiker verbonden is geweest in uren:

`ac`

- Toon hoe lang gebruikers verbonden zijn geweest in uren:

`ac --individual-totals`

- Toon hoe lang een bepaalde gebruiker verbonden is geweest in uren:

`ac --individual-totals `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Toon hoe lang een bepaalde gebruiker per dag verbonden is geweest in uren (met totaal):

`ac --daily-totals --individual-totals `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Toon ook extra details:

`ac --compatibility`
