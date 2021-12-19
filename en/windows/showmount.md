---
layout: page
title: windows/showmount (English)
description: "Display information about NFS filesystems on Windows Server."
content_hash: 888f48b7afea340dc888f8034481b248545e3821
---
# showmount

Display information about NFS filesystems on Windows Server.
More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/showmount>.

- Display all exported filesystems:

`showmount -e`

- Display all NFS clients and their mounted directories:

`showmount -a`

- Display all NFS mounted directories:

`showmount -d`

- Display all exported filesystems for a remote server:

`showmount -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_address</span>
