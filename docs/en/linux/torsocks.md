---
layout: page
title: linux/torsocks (English)
description: "Route the traffic of any application through the Tor network."
content_hash: 74ef2717521e207fc24f02584fb0441c51cd5bc4
last_modified_at: 2024-04-04
related_topics:
  - title: español version
    url: /es/linux/torsocks.html
    icon: bi bi-globe
tldri18n_status: 2
---
# torsocks

Route the traffic of any application through the Tor network.
Note: `torsocks` will assume that it should connect to the Tor SOCKS proxy running at 127.0.0.1:9050 being the defaults of the Tor daemon.
More information: <https://gitlab.torproject.org/tpo/core/torsocks/>.

- Run a command using Tor:

`torsocks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Enable or disable Tor in this shell:

`. torsocks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Spawn a new Tor enabled shell:

`torsocks --shell`

- Check if current shell is Tor enabled (`LD_PRELOAD` value will be empty if disabled):

`torsocks show`

- [i]solate traffic through a different Tor circuit, improving anonymity:

`torsocks --isolate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">curl https://check.torproject.org/api/ip</span>

- Connect to a Tor proxy running on a specific [a]ddress and [P]ort:

`torsocks --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
