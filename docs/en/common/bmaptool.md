---
layout: page
title: common/bmaptool (English)
description: "Create or copy block maps intelligently (designed to be faster than `cp` or `dd`)."
content_hash: 3b06fd07bf42b7594ca946c012c1214c3f375936
last_modified_at: 2024-02-19
related_topics:
  - title: italiano version
    url: /it/common/bmaptool.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bmaptool.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bmaptool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bmaptool

Create or copy block maps intelligently (designed to be faster than `cp` or `dd`).
More information: <https://source.tizen.org/documentation/reference/bmaptool>.

- [o]utput a blockmap file from image file:

`bmaptool create -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blockmap.bmap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.img</span>

- Copy an image file into sdb:

`bmaptool copy --bmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blockmap.bmap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.img</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb</span>

- Copy a compressed image file into sdb:

`bmaptool copy --bmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blockmap.bmap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.img.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb</span>

- Copy an image file into sdb without using a blockmap:

`bmaptool copy --nobmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.img</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb</span>
