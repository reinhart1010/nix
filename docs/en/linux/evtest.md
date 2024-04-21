---
layout: page
title: linux/evtest (English)
description: "Display information from input device drivers."
content_hash: efb57f4a46fb0aa4f7116faf5aa7760d34a94e1a
last_modified_at: 2024-04-21
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/evtest.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># evtest

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
