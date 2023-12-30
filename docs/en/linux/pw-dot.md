---
layout: page
title: linux/pw-dot (English)
description: "Create `.dot` files of the PipeWire graph."
content_hash: 2fbdf3bced7c1ac5dd9377a4a9bc6c31712829a7
last_modified_at: 2023-12-30
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pw-dot.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pw-dot

Create `.dot` files of the PipeWire graph.
See also: `dot`, for rendering graph.
More information: <https://docs.pipewire.org/page_man_pw-dot_1.html>.

- Generate a graph to `pw.dot` file:

`pw-dot`

- Specify an output file, showing all object types:

`pw-dot --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.dot</span>` --all`

- Print `.dot` graph to `stdout`, showing all object properties:

`pw-dot --output - --detail`

- Generate a graph from a remote instance, showing only linked objects:

`pw-dot --remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` --smart`

- Lay the graph from left to right, instead of dot's default top to bottom:

`pw-dot --lr`

- Lay the graph using 90-degree angles in edges:

`pw-dot --90`
