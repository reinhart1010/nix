---
layout: page
title: common/htmlq (English)
description: "Use CSS selectors to extract content from HTML files."
content_hash: 0353653563651c90608b732c3c3becca9d4a49c0
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/htmlq.html
    icon: bi bi-globe
tldri18n_status: 2
---
# htmlq

Use CSS selectors to extract content from HTML files.
More information: <https://github.com/mgdm/htmlq>.

- Return all elements of class `card`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.html</span>` | htmlq '.card'`

- Get the text content of the first paragraph:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.html</span>` | htmlq --text 'p:first-of-type'`

- Find all the links in a page:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.html</span>` | htmlq --attribute href 'a'`

- Remove all images and SVGs from a page:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.html</span>` | htmlq --remove-nodes 'img' --remove-nodes 'svg'`

- Pretty print and write the output to a file:

`htmlq --pretty --filename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.html</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.html</span>
