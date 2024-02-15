---
layout: page
title: common/dive (English)
description: "Explore a Docker image, layer contents, and discover ways to shrink it."
content_hash: 142816f2968740a2209110b75c7b29cd4588641b
last_modified_at: 2024-02-15
related_topics:
  - title: فارسی version
    url: /fa/common/dive.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dive.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dive.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dive

Explore a Docker image, layer contents, and discover ways to shrink it.
More information: <https://github.com/wagoodman/dive>.

- Analyze a Docker image:

`dive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">your_image_tag</span>

- Build an image and start analyzing it:

`dive build -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">some_tag</span>
