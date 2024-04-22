---
layout: page
title: linux/evtest (English)
description: "Display information from input device drivers."
content_hash: efb57f4a46fb0aa4f7116faf5aa7760d34a94e1a
last_modified_at: 2024-04-22
tldri18n_status: 2
---
# evtest

Display information from input device drivers.
More information: <https://manned.org/evtest>.

- List all detected input devices:

`sudo evtest`

- Display events from a specific input device:

`sudo evtest /dev/input/event`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>

- Grab the device exclusively, preventing other clients from receiving events:

`sudo evtest --grab /dev/input/event`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>

- Query the state of a specific key or button on an input device:

`sudo evtest --query /dev/input/event`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">event_type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">event_code</span>
