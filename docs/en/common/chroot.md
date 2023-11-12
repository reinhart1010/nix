---
layout: page
title: common/chroot (English)
description: "Run command or interactive shell with special root directory."
content_hash: 3452e81acd9235f247e74ccbc2cfb0656c44fd84
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/chroot.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chroot.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chroot.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chroot.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chroot.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/chroot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chroot

Run command or interactive shell with special root directory.
More information: <https://www.gnu.org/software/coreutils/chroot>.

- Run command as new root directory:

`chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/new/root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Specify user and group (ID or name) to use:

`chroot --userspec=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user:group</span>
