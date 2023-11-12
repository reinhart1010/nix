---
layout: page
title: linux/slop (English)
description: "Get a selection of the screen."
content_hash: 64877bac5cf329c6153060a9972f904d34624204
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# slop

Get a selection of the screen.
More information: <https://github.com/naelstrof/slop>.

- Wait for the user to make a selection and output its geometry to `stdout`:

`slop`

- Double click, rather than click and drag, to draw a selection:

`slop -D`

- Highlight the selection rather than outlining it:

`slop -l`

- Specify the output format:

`slop -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">format_string</span>

- Specify the selection rectangle's color:

`slop -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">red</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">green</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blue</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alpha</span>
