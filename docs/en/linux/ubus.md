---
layout: page
title: linux/ubus (English)
description: "Interact with an OpenWrt ubusd server."
content_hash: 90110afc4c9ba84eb2a16d1a57df5930ed8b686e
last_modified_at: 2025-03-03
tldri18n_status: 2
---
# ubus

Interact with an OpenWrt ubusd server.
More information: <https://openwrt.org/docs/techref/ubus>.

- List available objects:

`ubus list`

- Retrieve system information in JSON format:

`ubus call system board`

- Listen to events:

`ubus subscribe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">event_name</span>
