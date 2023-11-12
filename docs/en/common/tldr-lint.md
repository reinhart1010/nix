---
layout: page
title: common/tldr-lint (English)
description: "Lint and format `tldr` pages."
content_hash: 14200347f6c59ecf8986d88f9c646d0330494cd4
last_modified_at: 2023-11-12
related_topics:
  - title: polski version
    url: /pl/common/tldr-lint.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/tldr-lint.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/tldr-lint.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tldr-lint

Lint and format `tldr` pages.
More information: <https://github.com/tldr-pages/tldr-lint>.

- Lint all pages:

`tldr-lint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pages_directory</span>

- Format a specific page to `stdout`:

`tldr-lint --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">page.md</span>

- Format all pages in place:

`tldr-lint --format --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pages_directory</span>
