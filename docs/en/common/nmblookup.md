---
layout: page
title: common/nmblookup (English)
description: "Discover SMB shares."
content_hash: 053192d04a01816c3dd610afc5d4f994c82004d0
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# nmblookup

Discover SMB shares.
More information: <https://www.samba.org/samba/docs/current/man-html/nmblookup.1.html>.

- Find hosts in the local network with SMB shares:

`nmblookup -S '*'`

- Find hosts in the local network with SMB shares run by SAMBA:

`nmblookup --status __SAMBA__`
