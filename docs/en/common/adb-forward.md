---
layout: page
title: common/adb-forward (English)
description: "Connect to an Android device wirelessly."
content_hash: 15dc766ffed5d1dc957594013b3af21ba4f2c45e
last_modified_at: 2024-12-27
tldri18n_status: 2
---
# adb forward

Connect to an Android device wirelessly.
More information: <https://developer.android.com/tools/adb>.

- Forward a TCP port:

`adb forward tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_port</span>` tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_port</span>

- List all forwardings:

`adb forward --list`

- Remove a forwarding rule:

`adb forward --remove tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_port</span>

- Remove all forwarding rules:

`adb forward --remove-all`
