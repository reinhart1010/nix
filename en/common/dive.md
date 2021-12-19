---
layout: page
title: common/dive (English)
description: "A tool for exploring a Docker image, layer contents, and discovering ways to shrink it."
content_hash: da89b268a57d377de291d0188708cc8acac582e4
related_topics:
  - title: italiano version
    url: /it/common/dive.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dive.html
    icon: bi bi-globe
---
# dive

A tool for exploring a Docker image, layer contents, and discovering ways to shrink it.
More information: <https://github.com/wagoodman/dive>.

- Analyze a Docker image:

`dive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">your_image_tag</span>

- Build an image and start analyzing it:

`dive build -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">some_tag</span>
