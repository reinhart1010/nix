---
layout: page
title: linux/ptx (English)
description: "Generate a permuted index of words from text files."
content_hash: cc54905ec4e10026457bcaf473bef3381854dc06
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/linux/ptx.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/ptx.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ptx

Generate a permuted index of words from text files.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/ptx-invocation.html>.

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
