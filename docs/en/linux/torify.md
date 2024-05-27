---
layout: page
title: linux/torify (English)
description: "Route network traffic through the Tor network."
content_hash: 40a161895a375396248b249ca992015ec82e3125
last_modified_at: 2024-05-27
tldri18n_status: 2
---
# torify

Route network traffic through the Tor network.
Note: This command has been deprecated, and is now a backwards-compatible wrapper of `torsocks`.
More information: <https://manned.org/man/torify>.

- Route traffic via Tor:

`torify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Toggle Tor in shell:

`torify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Spawn a Tor-enabled shell:

`torify --shell`

- Check for a Tor-enabled shell:

`torify show`

- Specify Tor configuration file:

`torify -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">config-file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Use a specific Tor SOCKS proxy:

`torify -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proxy</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Redirect output to a file:

`torify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output</span>
