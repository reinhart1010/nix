---
layout: page
title: linux/debootstrap (English)
description: "Create a basic Debian system."
content_hash: aba09cf7432832437a642f6c172ecb7735fc6931
last_modified_at: 2023-11-12
related_topics:
  - title: Indonesia version
    url: /id/linux/debootstrap.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/debootstrap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# debootstrap

Create a basic Debian system.
More information: <https://wiki.debian.org/Debootstrap>.

- Create a Debian stable release system inside the `debian-root` directory:

`sudo debootstrap stable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/debian-root/</span>` http://deb.debian.org/debian`

- Create a minimal system including only required packages:

`sudo debootstrap --variant=minbase stable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/debian-root/</span>

- Create an Ubuntu 20.04 system inside the `focal-root` directory with a local mirror:

`sudo debootstrap focal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/focal-root/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file:///path/to/mirror/</span>

- Switch to a bootstrapped system:

`sudo chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/root</span>

- List available releases:

`ls /usr/share/debootstrap/scripts/`
