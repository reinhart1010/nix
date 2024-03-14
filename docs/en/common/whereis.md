---
layout: page
title: common/whereis (English)
description: "Locate the binary, source, and manual page files for a command."
content_hash: 1694fdd2c9ce8be859dc3de107cd86cd1a72965b
last_modified_at: 2024-03-14
related_topics:
  - title: فارسی version
    url: /fa/common/whereis.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/whereis.html
    icon: bi bi-globe
tldri18n_status: 2
---
# whereis

Locate the binary, source, and manual page files for a command.
More information: <https://manned.org/whereis>.

- Locate binary, source and man pages for SSH:

`whereis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh</span>

- Locate binary and man pages for ls:

`whereis -bm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>

- Locate source of gcc and man pages for Git:

`whereis -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gcc</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git</span>

- Locate binaries for gcc in `/usr/bin/` only:

`whereis -b -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/bin/</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gcc</span>

- Locate unusual binaries (those that have more or less than one binary on the system):

`whereis -u *`

- Locate binaries that have unusual manual entries (binaries that have more or less than one manual installed):

`whereis -u -m *`
