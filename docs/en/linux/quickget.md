---
layout: page
title: linux/quickget (English)
description: "Download and prepare materials for building a Quickemu virtual machine."
content_hash: 2d88644a31161379c07b84b3954865bf89430455
last_modified_at: 2024-09-08
tldri18n_status: 2
---
# quickget

Download and prepare materials for building a Quickemu virtual machine.
Note: the parameter "edition" is always optional.
See also: `quickemu`.
More information: <https://github.com/quickemu-project/quickemu>.

- Display the list of all supported guest operating systems, versions and variants:

`quickget list`

- Download and create the virtual machine configuration for building a Quickemu virtual machine for an OS:

`quickget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">os</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">release</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">edition</span>

- Download configuration for a Windows 11 VM with VirtIO drivers for Windows:

`quickget windows 11`

- Download a macOS recovery image and creates a virtual machine configuration:

`quickget macos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mojave|catalina|big-sur|monterey|ventura|sonoma</span>

- Show an ISO URL for an operating system:

`quickget --url fedora `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">release</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">edition</span>

- Test if an ISO file is available for an operating system:

`quickget --check nixos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">release</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">edition</span>

- Download an image without building any VM configuration:

`quickget --download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">os</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">release</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">edition</span>

- Create a VM configuration for an OS image:

`quickget --create-config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">os</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/iso</span>
