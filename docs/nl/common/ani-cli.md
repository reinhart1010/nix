---
layout: page
title: common/ani-cli (Nederlands)
description: "Een cli om door anime te bladeren en deze te bekijken."
content_hash: 7d471dc4d6c89f813b0c9571e2fa0ff05f22358d
last_modified_at: 2023-11-15
related_topics:
  - title: Deutsch version
    url: /de/common/ani-cli.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ani-cli.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ani-cli.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ani-cli.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/common/ani-cli.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ani-cli.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ani-cli.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ani-cli

Een cli om door anime te bladeren en deze te bekijken.
Meer informatie: <https://github.com/pystardust/ani-cli>.

- Zoek naar anime op naam:

`ani-cli "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anime_naam</span>`"`

- Download aflevering:

`ani-cli -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anime_naam</span>`"`

- Gebruik VLC als de media player:

`ani-cli -v "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anime_naam</span>`"`

- Specificeer een aflevering om te kijken:

`ani-cli -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">afleveringnummer</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anime_naam</span>`"`

- Bekijk anime uit je geschiedenis:

`ani-cli -c`

- Update `ani-cli`:

`ani-cli -U`
