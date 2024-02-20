---
layout: page
title: common/golangci-lint (English)
description: "Parallelized, smart and fast Go linters runner that integrates with all major IDEs and supports YAML configuration."
content_hash: 3561cc6f0b79147b8f5a80318856381122c8b959
last_modified_at: 2024-02-20
tldri18n_status: 2
---
# golangci-lint

Parallelized, smart and fast Go linters runner that integrates with all major IDEs and supports YAML configuration.
More information: <https://golangci-lint.run/usage/quick-start/>.

- Run linters in the current folder:

`golangci-lint run`

- List enabled and disabled linters (Note: disabled linters are shown last, do not mistake them for enabled ones):

`golangci-lint linters`

- [E]nable a specific linter for this run:

`golangci-lint run --enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linter</span>
