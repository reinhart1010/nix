---
layout: page
title: linux/ptx (English)
description: "Generate a permuted index of words from text files."
content_hash: d32e50e68e2394bd2a6b909f900c26663b05f2b0
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# ptx

Generate a permuted index of words from text files.
More information: <https://www.gnu.org/software/coreutils/ptx>.

- Generate a permuted index where the first field of each line is an index reference:

`ptx --references `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Generate a permuted index with automatically generated index references:

`ptx --auto-reference `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Generate a permuted index with a fixed width:

`ptx --width=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width_in_columns</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Generate a permuted index with a list of filtered words:

`ptx --only-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filter</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Generate a permuted index with SYSV-style behaviors:

`ptx --traditional `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
