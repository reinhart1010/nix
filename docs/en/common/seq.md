---
layout: page
title: common/seq (English)
description: "Output a sequence of numbers to `stdout`."
content_hash: 175951a2631ba2d45d845b81860019218e647e12
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/seq.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/seq.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/seq.html
    icon: bi bi-globe
tldri18n_status: 2
---
# seq

Output a sequence of numbers to `stdout`.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/seq-invocation.html>.

- Sequence from 1 to 10:

`seq 10`

- Every 3rd number from 5 to 20:

`seq 5 3 20`

- Separate the output with a space instead of a newline:

`seq -s " " 5 3 20`

- Format output width to a minimum of 4 digits padding with zeros as necessary:

`seq -f "%04g" 5 3 20`
