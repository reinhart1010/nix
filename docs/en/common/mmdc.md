---
layout: page
title: common/mmdc (English)
description: "CLI for mermaid, a diagram generation tool with a domain-specific language."
content_hash: a1eef6f97cc7623a97337d36779dd53d95c8f53d
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mmdc

CLI for mermaid, a diagram generation tool with a domain-specific language.
A mermaid definition file is taken as input and a SVG, PNG, or PDF file is generated as output.
More information: <https://mermaid-js.github.io/mermaid/>.

- Convert a file to the specified format (automatically determined from the file extension):

`mmdc --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.mmd</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.svg</span>

- Specify the theme of the chart:

`mmdc --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.mmd</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.svg</span>` --theme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">forest|dark|neutral|default</span>

- Specify the background color of the chart (e.g. `lime`, `"#D8064F"`, or `transparent`):

`mmdc --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.mmd</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.svg</span>` --backgroundColor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">color</span>
