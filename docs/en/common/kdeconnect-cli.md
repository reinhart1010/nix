---
layout: page
title: common/kdeconnect-cli (English)
description: "Use KDE Connect for sharing files or text to a device, ringing it, unlocking it, and much more."
content_hash: b6809876f2962bd7250fa1243835a804b28979d9
last_modified_at: 2024-03-08
tldri18n_status: 2
---
# kdeconnect-cli

Use KDE Connect for sharing files or text to a device, ringing it, unlocking it, and much more.
More information: <https://kdeconnect.kde.org>.

- List all devices:

`kdeconnect-cli --list-devices`

- List available (paired and reachable) devices:

`kdeconnect-cli --list-available`

- Request pairing with a specific device, specifying its ID:

`kdeconnect-cli --pair --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_id</span>

- Ring a device, specifying its name:

`kdeconnect-cli --ring --name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_name</span>`"`

- Share an URL or file with a paired device, specifying its ID:

`kdeconnect-cli --share `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|path/to/file</span>` --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_id</span>

- Send an SMS with an optional attachment to a specific number:

`kdeconnect-cli --name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_name</span>`" --send-sms "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`" --destination `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">phone_number</span>` --attachment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Unlock a specific device:

`kdeconnect-cli --name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_name</span>`" --unlock`

- Simulate a key press on a specific device:

`kdeconnect-cli --name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_name</span>`" --send-keys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>
