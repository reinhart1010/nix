---
layout: page
title: osx/tart (English)
description: "Build, run and manage macOS and Linux virtual machines (VMs) on Apple Silicon."
content_hash: 6f5561a9753b3a901c362605b1f9845b69adf605
last_modified_at: 2022-12-17
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># tart

Build, run and manage macOS and Linux virtual machines (VMs) on Apple Silicon.
More information: <https://github.com/cirruslabs/tart>.

- Pull a remote VM image:

`tart pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">acme.io/org/name:tag</span>

- Clone a VM from a local or remote image source:

`tart clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source-vm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm-name</span>

- Create a new Mac VM from a specific ipsw file:

`tart create --from-ipsw=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">latest|path/to/file.ipsw</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm-name</span>

- Run an existing VM:

`tart run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm-name</span>

- Run an existing VM with a specific mounted directory:

`tart run --dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/local_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm-name</span>

- List VMs:

`tart list`

- Get IP address of a running VM:

`tart ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm-name</span>

- Change a VM's display resolution:

`tart set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm-name</span>` --display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>
