---
layout: page
title: common/fold (English)
description: "Wraps each line in an input file to fit a specified width and prints it to the standard output."
content_hash: f6dbe240374e0de72e25dee608d7216f8bcd5821
---
# fold

Wraps each line in an input file to fit a specified width and prints it to the standard output.
More information: <https://www.gnu.org/software/coreutils/fold>.

- Wrap each line to default width (80 characters):

`fold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Wrap each line to width "30":

`fold -w30 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Wrap each line to width "5" and break the line at spaces (puts each space separated word in a new line, words with length > 5 are wrapped):

`fold -w5 -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>
