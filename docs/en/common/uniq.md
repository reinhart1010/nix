---
layout: page
title: common/uniq (English)
description: "Output the unique lines from a input or file."
content_hash: daab1b9c2c8009121dcb9bf7328010495d29542f
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/uniq.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/uniq.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/uniq.html
    icon: bi bi-globe
tldri18n_status: 2
---
# uniq

Output the unique lines from a input or file.
Since it does not detect repeated lines unless they are adjacent, we need to sort them first.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/uniq-invocation.html>.

- Display each line once:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | uniq`

- Display only unique lines:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | uniq -u`

- Display only duplicate lines:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | uniq -d`

- Display number of occurrences of each line along with that line:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | uniq -c`

- Display number of occurrences of each line, sorted by the most frequent:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | uniq -c | sort -nr`
