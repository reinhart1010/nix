---
layout: page
title: osx/tart (English)
description: "Build, run and manage macOS and Linux virtual machines (VMs) on Apple Silicon."
content_hash: 539ae0d86d822bf51402dc3dd120e3432f1dd396
last_modified_at: 2023-02-20
---
# tart

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

`tart set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm-name</span>` --display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">640</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">400</span>
