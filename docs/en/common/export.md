---
layout: page
title: common/export (English)
description: "Command to mark shell variables in the current environment to be exported with any newly forked child processes."
content_hash: c26e5f26647738005f1400fcec3f9c040e7fe72f
last_modified_at: 2023-11-12
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
More information: <https://www.gnu.org/software/bash/manual/bash.html#index-export>.

- Set a new environment variable:

`export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VARIABLE</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Remove an environment variable:

`export -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VARIABLE</span>

- Mark a shell function for export:

`export -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FUNCTION_NAME</span>

- Append something to the PATH variable:

`export PATH=$PATH:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/append</span>
