---
layout: page
title: common/fold (English)
description: "Wrap each line in an input file to fit a specified width and print it to `stdout`."
content_hash: e0a6491ef5cb0285f7f55b56e16f1911613f3774
last_modified_at: 2023-08-09
---
# fold

Wrap each line in an input file to fit a specified width and print it to `stdout`.
More information: <https://manned.org/fold.1p>.

- Wrap each line to default width (80 characters):

`fold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Wrap each line to width "30":

`fold -w30 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Wrap each line to width "5" and break the line at spaces (puts each space separated word in a new line, words with length > 5 are wrapped):

`fold -w5 -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
