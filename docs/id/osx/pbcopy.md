---
layout: page
title: osx/pbcopy (Indonesia)
description: "Menempatkan output standar pada papan klip (clipboard)."
content_hash: f2890db98d937a69e6018f9465fea5879eed4880
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/pbcopy.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/pbcopy.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/osx/pbcopy.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/pbcopy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pbcopy

Menempatkan output standar pada papan klip (clipboard).
Informasi lebih lanjut: <https://keith.github.io/xcode-man-pages/pbcopy.1.html>.

- Menempatkan konten file pada papan klip:

`pbcopy < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Menempatkan hasil perintah pada papan klip:

`find . -type t -name "*.png" | pbcopy`
