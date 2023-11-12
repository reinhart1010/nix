---
layout: page
title: common/parallel (English)
description: "Run commands on multiple CPU cores."
content_hash: a4d2177277f5702fc76bca89b5fd0f60c1a656e8
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# parallel

Run commands on multiple CPU cores.
More information: <https://www.gnu.org/software/parallel>.

- Gzip several files at once, using all cores:

`parallel gzip ::: `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file3</span>

- Read arguments from `stdin`, run 4 jobs at once:

`ls *.txt | parallel -j4 gzip`

- Convert JPG images to PNG using replacement strings:

`parallel convert {} {.}.png ::: *.jpg`

- Parallel xargs, cram as many args as possible onto one command:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">args</span>` | parallel -X `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Break `stdin` into ~1M blocks, feed each block to `stdin` of new command:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">big_file.txt</span>` | parallel --pipe --block 1M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Run on multiple machines via SSH:

`parallel -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">machine1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">machine2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` ::: `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arg1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arg2</span>
