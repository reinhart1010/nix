---
layout: page
title: common/distccd (English)
description: "Server daemon for the distcc distributed compiler."
content_hash: 8a463eb3e0a4f6dfdc4fff4199c55f45e0ecb0fe
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# distccd

Server daemon for the distcc distributed compiler.
More information: <https://distcc.github.io>.

- Start a daemon with the default settings:

`distccd --daemon`

- Start a daemon, accepting connections from IPv4 private network ranges:

`distccd --daemon --allow-private`

- Start a daemon, accepting connections from a specific network address or address range:

`distccd --daemon --allow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address|network_prefix</span>

- Start a daemon with a lowered priority that can run a maximum of 4 tasks at a time:

`distccd --daemon --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` --nice `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Start a daemon and register it via mDNS/DNS-SD (Zeroconf):

`distccd --daemon --zeroconf`
