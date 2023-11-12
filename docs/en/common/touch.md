---
layout: page
title: common/touch (English)
description: "Create files and set access/modification times."
content_hash: 530c8cedbf62f052269f89bc4bef74b5db164ecf
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/common/touch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/touch.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/touch.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/touch.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/touch.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/touch.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/touch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# touch

Create files and set access/modification times.
More information: <https://manned.org/man/freebsd-13.1/touch>.

- Create specific files:

`touch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Set the file [a]ccess or [m]odification times to the current one and don't [c]reate file if it doesn't exist:

`touch -c -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a|m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Set the file [t]ime to a specific value and don't [c]reate file if it doesn't exist:

`touch -c -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYYMMDDHHMM.SS</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Set the file time of a specific file to the time of anothe[r] file and don't [c]reate file if it doesn't exist:

`touch -c -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.emacs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>
