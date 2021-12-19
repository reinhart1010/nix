---
layout: page
title: linux/pihole (English)
description: "Terminal interface for the Pi-hole ad-blocking DNS server."
content_hash: 9fa0a13803bd55ab06f7e512e443dd28522f4f1a
---
# pihole

Terminal interface for the Pi-hole ad-blocking DNS server.
More information: <https://pi-hole.net>.

- Check the Pi-hole daemon's status:

`pihole status`

- Update Pi-hole:

`pihole updatePihole`

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
