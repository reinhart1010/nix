---
layout: page
title: linux/pihole (English)
description: "Terminal interface for the Pi-hole ad-blocking DNS server."
content_hash: 5addb6cc796e957d63e585aa6bb37ffaae9e1423
---
# pihole

Terminal interface for the Pi-hole ad-blocking DNS server.
More information: <https://docs.pi-hole.net/core/pihole-command/>.

- Check the Pi-hole daemon's status:

`pihole status`

- Update Pi-hole and Gravity:

`pihole -up`

- Monitor detailed system status:

`pihole chronometer`

- Start or stop the daemon:

`pihole `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>

- Restart the daemon (not the server itself):

`pihole restartdns`

- Whitelist or blacklist a domain:

`pihole `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">whitelist|blacklist</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Search the lists for a domain:

`pihole query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Open a real-time log of connections:

`pihole tail`
