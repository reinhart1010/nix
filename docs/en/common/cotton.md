---
layout: page
title: common/cotton (English)
description: "Markdown test specification runner."
content_hash: 9d438ad47a61b71654dd6ee38c803987ed5e5f2c
related_topics:
  - title: 한국어 version
    url: /ko/common/cotton.html
    icon: bi bi-globe
---
# cotton

Markdown test specification runner.
More information: <https://github.com/chonla/cotton>.

- Use a specific base URL:

`cotton -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base_url</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>`.md`

- Disable certificate verification (insecure mode):

`cotton -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base_url</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>`.md`

- Stop running when a test fails:

`cotton -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base_url</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>`.md`
