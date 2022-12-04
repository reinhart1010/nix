---
layout: page
title: common/fold (English)
description: "Wraps each line in an input file to fit a specified width and prints it to the standard output."
content_hash: b01ee773754880b2371af2aae0d9f5ce857e1993
last_modified_at: 2022-12-04
---
# fold

Wraps each line in an input file to fit a specified width and prints it to the standard output.
More information: <https://www.gnu.org/software/coreutils/fold>.

- Wrap each line to default width (80 characters):

`fold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Wrap each line to width "30":

`fold -w30 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Wrap each line to width "5" and break the line at spaces (puts each space separated word in a new line, words with length > 5 are wrapped):

`fold -w5 -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
