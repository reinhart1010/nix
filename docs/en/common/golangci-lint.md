---
layout: page
title: common/golangci-lint (English)
description: "Parallelized, smart and fast Go linters runner that integrates with all major IDEs and supports YAML configuration."
content_hash: f6c2836cd8c1c35562ce0e7c78ad10cf7cce2f07
last_modified_at: 2024-05-23
related_topics:
  - title: español version
    url: /es/common/golangci-lint.html
    icon: bi bi-globe
tldri18n_status: 2
---
# golangci-lint

Parallelized, smart and fast Go linters runner that integrates with all major IDEs and supports YAML configuration.
More information: <https://golangci-lint.run/welcome/quick-start/>.

- Run linters in the current folder:

`golangci-lint run`

- List enabled and disabled linters (Note: disabled linters are shown last, do not mistake them for enabled ones):

`golangci-lint linters`

- [E]nable a specific linter for this run:

`golangci-lint run --enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linter</span>
