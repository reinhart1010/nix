---
layout: page
title: linux/eselect-locale (Nederlands)
description: "Een `eselect`-module voor het beheren van de `LANG`-omgevingsvariabele, die de systeemtaal instelt."
content_hash: 85e7c57f7ebeb61603c09420099651e7691ebcc0
last_modified_at: 2024-07-20
related_topics:
  - title: English version
    url: /en/linux/eselect-locale.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/eselect-locale.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># eselect locale

Een `eselect`-module voor het beheren van de `LANG`-omgevingsvariabele, die de systeemtaal instelt.
Meer informatie: <https://wiki.gentoo.org/wiki/Eselect#Locale>.

- Lijst van beschikbare locales:

`eselect locale list`

- Stel de `LANG`-omgevingsvariabele in `/etc/profile.env` in op naam of index van de `list`-opdracht:

`eselect locale set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">naam|index</span>

- Toon de waarde van `LANG` in `/etc/profile.env`:

`eselect locale show`
