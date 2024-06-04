---
layout: page
title: linux/pw-dot (English)
description: "Create `.dot` files of the PipeWire graph."
content_hash: abf68465a193e0fe76ab9bcf0e08bf5f3a1b9241
last_modified_at: 2024-06-04
tldri18n_status: 2
---
# pw-dot

Create `.dot` files of the PipeWire graph.
See also: `dot`, for rendering graph.
More information: <https://docs.pipewire.org/page_man_pw-dot_1.html>.

- Generate a graph to `pw.dot` file:

`pw-dot`

- Read objects from `pw-dump` JSON file:

`pw-dot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-j|--json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.json</span>

- Specify an [o]utput file, showing [a]ll object types:

`pw-dot --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.dot</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--all</span>

- Print `.dot` graph to `stdout`, showing all object properties:

`pw-dot --output - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--detail</span>

- Generate a graph from a [r]emote instance, showing only linked objects:

`pw-dot --remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--smart</span>

- Lay the graph from [l]eft to [r]ight, instead of dot's default top to bottom:

`pw-dot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-L|--lr</span>

- Lay the graph using 90-degree angles in edges:

`pw-dot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-9|--90</span>

- Display help:

`pw-dot --help`
