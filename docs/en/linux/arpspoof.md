---
layout: page
title: linux/arpspoof (English)
description: "Forge ARP replies to intercept packets."
content_hash: e20b1d0c8176a0e5cb1bc3830fa222ad266ff827
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# arpspoof

Forge ARP replies to intercept packets.
More information: <https://monkey.org/~dugsong/dsniff>.

- Poison all hosts to intercept packets on [i]nterface for the host:

`sudo arpspoof -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_ip</span>

- Poison [t]arget to intercept packets on [i]nterface for the host:

`sudo arpspoof -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_ip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_ip</span>

- Poison both [t]arget and host to intercept packets on [i]nterface for the host:

`sudo arpspoof -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>` -r -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_ip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_ip</span>
