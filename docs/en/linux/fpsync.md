---
layout: page
title: linux/fpsync (English)
description: "Execute several synchronization processes locally or on several remote workers through SSH."
content_hash: 10915a5fd7cbe8b508e6c7d4f4cb07790d3ecdff
last_modified_at: 2024-06-28
tldri18n_status: 2
---
# fpsync

Execute several synchronization processes locally or on several remote workers through SSH.
More information: <https://www.fpart.org/fpsync/>.

- Recursively synchronize a directory to another location:

`fpsync -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/source/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/destination/</span>

- Recursively synchronize a directory with the final pass (It enables rsync's `--delete` option with each synchronization job):

`fpsync -v -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/source/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/destination/</span>

- Recursively synchronize a directory to a destination using 8 concurrent synchronization jobs:

`fpsync -v -n 8 -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/source/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/destination/</span>

- Recursively synchronize a directory to a destination using 8 concurrent synchronization jobs spread over two remote workers (machine1 and machine2):

`fpsync -v -n 8 -E -w login@machine1 -w login@machine2 -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/shared/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/source/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/destination/</span>

- Recursively synchronize a directory to a destination using 4 local workers, each one transferring at most 1000 files and 100 MB per synchronization job:

`fpsync -v -n 4 -f 1000 -s $((100 * 1024 * 1024)) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/source/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/destination/</span>

- Recursively synchronize any directories but exclude specific `.snapshot*` files (Note: options and values must be separated by a pipe character):

`fpsync -v -O "-x|.snapshot*" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/source/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/destination/</span>
