---
layout: page
title: linux/modprobe (English)
description: "Add or remove modules from the Linux kernel."
content_hash: ea20081b4ec5fab79cfd3dbf36ec1ec5f07bf4fc
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/linux/modprobe.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/modprobe.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/modprobe.html
    icon: bi bi-globe
tldri18n_status: 2
---
# modprobe

Add or remove modules from the Linux kernel.
See also: `kmod`, for other module management commands.
More information: <https://manned.org/modprobe>.

- Pretend to load a module into the kernel, but don't actually do it:

`sudo modprobe --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Load a module into the kernel:

`sudo modprobe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Remove a module from the kernel:

`sudo modprobe --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Remove a module and those that depend on it from the kernel:

`sudo modprobe --remove-dependencies `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Show a kernel module's dependencies:

`sudo modprobe --show-depends `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>
