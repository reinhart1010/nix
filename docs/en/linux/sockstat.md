---
layout: page
title: linux/sockstat (English)
description: "List open Internet or UNIX domain sockets."
content_hash: b9e76028b5a9be930bf8388b1d1e6decbe1d4994
last_modified_at: 2024-01-16
tldri18n_status: 2
---
# sockstat

List open Internet or UNIX domain sockets.
See also: `netstat`.
More information: <https://manned.org/sockstat>.

- Show information for IPv4 and IPv6 sockets for both listening and connected sockets:

`sockstat`

- Show information for IPv[4]/IPv[6] sockets [l]istening on specific [p]orts using a specific p[R]otocol:

`sockstat -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4|6</span>` -l -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp|udp|raw|unix</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port1,port2...</span>

- Also show [c]onnected sockets and [u]nix sockets:

`sockstat -cu`

- Only show sockets of the specified `pid` or process:

`sockstat -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid|process</span>

- Only show sockets of the specified `uid` or user:

`sockstat -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|user</span>

- Only show sockets of the specified `gid` or group:

`sockstat -G `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gid|group</span>
