---
layout: page
title: common/cotton (English)
description: "Markdown test specification runner."
content_hash: ed097dddddd8d66f39b08bc821a08db421ccf738
last_modified_at: 2023-11-12
related_topics:
  - title: 한국어 version
    url: /ko/common/cotton.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cotton

Markdown test specification runner.
More information: <https://github.com/chonla/cotton>.

- Use a specific base URL:

`cotton -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base_url</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`.md`

- Disable certificate verification (insecure mode):

`cotton -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base_url</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`.md`

- Stop running when a test fails:

`cotton -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base_url</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`.md`
