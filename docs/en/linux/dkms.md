---
layout: page
title: linux/dkms (English)
description: "A framework that allows for dynamic building of kernel modules."
content_hash: af6e4f60975f7673b77718d9ec2df3c73b6fe65f
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# dkms

A framework that allows for dynamic building of kernel modules.
More information: <https://github.com/dell/dkms>.

- List currently installed modules:

`dkms status`

- Rebuild all modules for the currently running kernel:

`dkms autoinstall`

- Install version 1.2.1 of the acpi_call module for the currently running kernel:

`dkms install -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">acpi_call</span>` -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.1</span>

- Remove version 1.2.1 of the acpi_call module from all kernels:

`dkms remove -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">acpi_call</span>` -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.1</span>` --all`
