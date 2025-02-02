---
layout: page
title: common/nxc-nfs (English)
description: "Pentest and exploit NFS servers. Currently supports anonymous mode only."
content_hash: 71057ff4016fd243619368eb9e031576afc7465b
last_modified_at: 2024-10-29
tldri18n_status: 2
---
# nxc nfs

Pentest and exploit NFS servers. Currently supports anonymous mode only.
More information: <https://www.netexec.wiki/nfs-protocol>.

- Detect the version of a remote NFS server:

`nxc nfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.0/24</span>

- List the available NFS shares:

`nxc nfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2</span>` --shares`

- Enumerate the exposed shares recursively to the specified depth:

`nxc nfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2</span>` --enum-shares `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Download the specified remote file:

`nxc nfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2</span>` --get-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/remote_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/local_file</span>

- Upload the specified local file to the remote share:

`nxc nfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2</span>` --put-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/local_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/remote_file</span>
