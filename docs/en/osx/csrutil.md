---
layout: page
title: osx/csrutil (English)
description: "Manage the System Integrity Protection configuration."
content_hash: a0b5f1296eb6a0dde2fa9e80382421bb31309dce
---
# csrutil

Manage the System Integrity Protection configuration.
More information: <https://ss64.com/osx/csrutil.html>.

- Display the System Integrity Protection status:

`csrutil status`

- Disable the System Integrity Protection:

`csrutil disable`

- Enable the System Integrity Protection:

`csrutil enable`

- Display the list of allowed NetBoot sources:

`csrutil netboot list`

- Add an IPv4 address to the list of allowed NetBoot sources:

`csrutil netboot add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>

- Reset the System Integrity Protection status and clear the NetBoot list:

`csrutil clear`
