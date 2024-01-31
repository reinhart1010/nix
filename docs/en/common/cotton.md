---
layout: page
title: common/cotton (English)
description: "Markdown test specification runner."
content_hash: a56deae6e071f559e8fb050e8f14d8e6cf93ad9d
last_modified_at: 2024-01-31
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

`cotton -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base_url</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.md</span>

- Disable certificate verification (insecure mode):

`cotton -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base_url</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.md</span>

- Stop running when a test fails:

`cotton -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base_url</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.md</span>
