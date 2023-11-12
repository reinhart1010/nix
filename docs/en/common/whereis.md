---
layout: page
title: common/whereis (English)
description: "Locate the binary, source, and manual page files for a command."
content_hash: 6dd5ce2ede6ce161921e72bd311c4ab6c1365a27
last_modified_at: 2023-11-12
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

- Locate binary, source and man pages for ssh:

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
