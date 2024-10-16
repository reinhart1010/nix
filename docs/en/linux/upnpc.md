---
layout: page
title: linux/upnpc (English)
description: "Configure port forwarding rules on your router via the UPnP protocol."
content_hash: 081a1bcef964fce96e4c2b9d9e442dfc67c5f121
last_modified_at: 2024-10-16
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/upnpc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># upnpc

Configure port forwarding rules on your router via the UPnP protocol.
More information: <https://manned.org/upnpc>.

- Forward the external TCP port 80 to port 8080 on a local machine:

`upnpc -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1</span>` 8080 80 tcp`

- Delete any port redirection for external TCP port 80:

`upnpc -d 80 tcp`

- Get information about UPnP devices on your network:

`upnpc -s`

- List existing redirections:

`upnpc -l`
