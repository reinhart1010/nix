---
layout: page
title: common/uv-tree (English)
description: "Display project dependencies in a tree format."
content_hash: 6e9b01b55379959b8c58de9000b1ac588d8d0a20
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/uv-tree.html
    icon: bi bi-globe
tldri18n_status: 2
---
# uv tree

Display project dependencies in a tree format.
More information: <https://docs.astral.sh/uv/reference/cli/#uv-tree>.

- Show dependency tree for current environment:

`uv tree`

- Show dependency tree for all environments:

`uv tree --universal`

- Show dependency tree up to a certain depth:

`uv tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--depth</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

- Show the latest available version for all outdated packages:

`uv tree --outdated`

- Exclude dependencies from the dev group:

`uv tree --no-dev`

- Show the inverted tree, so children are dependents instead of dependencies:

`uv tree --invert`
