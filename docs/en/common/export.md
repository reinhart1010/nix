---
layout: page
title: common/export (English)
description: "Command to mark shell variables in the current environment to be exported with any newly forked child processes."
content_hash: 2143761165d9b5c2f208335f8c3f22bded1e8bf5
last_modified_at: 2023-12-29
related_topics:
  - title: Deutsch version
    url: /de/common/export.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/export.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/export.html
    icon: bi bi-globe
tldri18n_status: 2
---
# export

Command to mark shell variables in the current environment to be exported with any newly forked child processes.
More information: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#export>.

- Set a new environment variable:

`export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VARIABLE</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Append something to the PATH variable:

`export PATH=$PATH:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/append</span>
