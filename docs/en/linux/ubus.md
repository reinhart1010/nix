---
layout: page
title: linux/ubus (English)
description: "Interact with an OpenWrt ubusd server."
content_hash: 90110afc4c9ba84eb2a16d1a57df5930ed8b686e
last_modified_at: 2025-03-02
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ubus.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ubus

Interact with an OpenWrt ubusd server.
More information: <https://openwrt.org/docs/techref/ubus>.

- List available objects:

`ubus list`

- Retrieve system information in JSON format:

`ubus call system board`

- Listen to events:

`ubus subscribe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">event_name</span>
