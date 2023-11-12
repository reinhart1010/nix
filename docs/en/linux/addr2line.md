---
layout: page
title: linux/addr2line (English)
description: "Convert addresses of a binary into file names and line numbers."
content_hash: ab687241983f529192257f45d78cbafbac81ccdc
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/addr2line.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/addr2line.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/addr2line.html
    icon: bi bi-globe
tldri18n_status: 2
---
# addr2line

Convert addresses of a binary into file names and line numbers.
More information: <https://manned.org/addr2line>.

- Display the filename and line number of the source code from an instruction address of an executable:

`addr2line --exe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/executable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>

- Display the function name, filename and line number:

`addr2line --exe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/executable</span>` --functions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>

- Demangle the function name for C++ code:

`addr2line --exe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/executable</span>` --functions --demangle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>
