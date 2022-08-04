---
layout: page
title: common/pup (English)
description: "Command-line HTML parsing tool."
content_hash: 64328a228c0a8a3816da3d7200ad520488d10ab5
---
# pup

Command-line HTML parsing tool.
More information: <https://github.com/ericchiang/pup>.

- Transform a raw HTML file into a cleaned, indented, and colored format:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index.html</span>` | pup --color`

- Filter HTML by element tag name:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index.html</span>` | pup '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>`'`

- Filter HTML by id:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index.html</span>` | pup '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">div#id</span>`'`

- Filter HTML by attribute value:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index.html</span>` | pup '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input[type="text"]</span>`'`

- Print all text from the filtered HTML elements and their children:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index.html</span>` | pup '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">div</span>` text{}'`

- Print HTML as JSON:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index.html</span>` | pup '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">div</span>` json{}'`
