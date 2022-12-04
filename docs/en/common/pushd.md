---
layout: page
title: common/pushd (English)
description: "Place a directory on a stack so it can be accessed later."
content_hash: 89fedd8ad3c8cd4f20186d45736ba834be45e611
last_modified_at: 2022-12-04
related_topics:
  - title: dansk version
    url: /da/common/pushd.html
    icon: bi bi-globe
---
# pushd

Place a directory on a stack so it can be accessed later.
See also `popd` to switch back to original directory and `dirs` to display directory stack contents.

- Switch to directory and push it on the stack:

`pushd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Switch first and second directories on the stack:

`pushd`

- Rotate stack by making the 5th element the top of the stack:

`pushd +4`
