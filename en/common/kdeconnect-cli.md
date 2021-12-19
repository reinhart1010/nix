---
layout: page
title: common/kdeconnect-cli (English)
description: "KDE Connect CLI."
content_hash: da580e874911de8983b799922393f1284b855158
---
# kdeconnect-cli

KDE Connect CLI.
More information: <https://kdeconnect.kde.org>.

- List all devices:

`kdeconnect-cli --list-devices`

- List available (paired and reachable) devices:

`kdeconnect-cli --list-available`

- Request pairing with a specific device, specifying its ID:

`kdeconnect-cli --pair --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_id</span>

- Ring a device, specifying its name:

`kdeconnect-cli --ring --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_name</span>

- Share an URL or file with a paired device, specifying its ID:

`kdeconnect-cli --share `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">URL|path/to/file</span>` --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_id</span>

- Send an SMS with an optional attachment to a specific number:

`kdeconnect-cli --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_name</span>` --send-sms `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>` --destination `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">phone_number</span>` --attachment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Unlock a specific device:

`kdeconnect-cli --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_name</span>` --unlock`

- Simulate a key press on a specific device:

`kdeconnect-cli --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device_name</span>` --send-keys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>
