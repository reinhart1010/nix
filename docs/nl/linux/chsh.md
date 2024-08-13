---
layout: page
title: linux/chsh (Nederlands)
description: "Verander de login shell van een gebruiker."
content_hash: aa218566de6d39210f92534b7b17f203ba2f9c54
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/linux/chsh.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/chsh.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chsh

Verander de login shell van een gebruiker.
Onderdeel van `util-linux`.
Meer informatie: <https://manned.org/chsh>.

- Stel een specifieke login shell interactief in voor de huidige gebruiker:

`sudo chsh`

- Stel een specifieke login[s]hell in voor de huidige gebruiker:

`sudo chsh --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/shell</span>

- Stel een login[s]hell in voor een specifieke gebruiker:

`sudo chsh --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Toon ([l]) beschikbare shells:

`sudo chsh --list-shells`
