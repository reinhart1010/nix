---
layout: page
title: linux/libuser-lid (Nederlands)
description: "Toon de groepen van een gebruiker of de gebruikers van een groep."
content_hash: 7d8dd4da656de29b4b7b8ac6615142536da3b54c
last_modified_at: 2024-01-11
related_topics:
  - title: English version
    url: /en/linux/libuser-lid.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/libuser-lid.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># libuser-lid

Toon de groepen van een gebruiker of de gebruikers van een groep.
In Fedora en Arch Linux is dit programma geïnstalleerd als `lid`.
Meer informatie: <https://manned.org/lid.8>.

- Toon primaire en secundaire groepen van een specifieke gebruiker:

`sudo lid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Toon gebruikers van een specifieke groep:

`sudo lid --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">naam</span>
