---
layout: page
title: linux/quickget (English)
description: "Download and prepare materials for building a Quickemu virtual machine."
content_hash: a81ea804a6b374944d8bed6eb3978ceac882e373
last_modified_at: 2024-02-05
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

`quickget macos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">high-sierra|mojave|catalina|big-sur|monterey|ventura</span>

- Show an ISO URL for an operating system (Note: it does not work for Windows):

`quickget --show-iso-url fedora `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">release</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">edition</span>

- Test if an ISO file is available for an operating system:

`quickget --test-iso-url nixos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">edition</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plasma5</span>

- Open an operating system distribution's homepage in a browser (Note: it does not work for Windows):

`quickget --open-distro-homepage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">os</span>
