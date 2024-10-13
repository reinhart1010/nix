---
layout: page
title: osx/base64 (Nederlands)
description: "Encodeer en decodeer met behulp van Base64-representatie."
content_hash: ab0513ccb6d0c4c6bfec165336396ea838ea88e4
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/osx/base64.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/base64.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/osx/base64.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/base64.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/base64.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/base64.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/base64.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># base64

Encodeer en decodeer met behulp van Base64-representatie.
Meer informatie: <https://keith.github.io/xcode-man-pages/base64.1.html>.

- Encodeer een bestand:

`base64 --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gewoon_bestand</span>

- Decodeer een bestand:

`base64 --decode --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base64_bestand</span>

- Encodeer vanaf `stdin`:

`echo -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">platte_tekst</span>`" | base64`

- Decodeer vanaf `stdin`:

`echo -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base64_tekst</span>` | base64 --decode`
