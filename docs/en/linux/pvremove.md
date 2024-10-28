---
layout: page
title: linux/pvremove (English)
description: "Remove LVM labels from physical volume(s)."
content_hash: 2a52668f36bf62b6711a6306d625c55b4950dc9e
last_modified_at: 2024-10-28
tldri18n_status: 2
---
# pvremove

Remove LVM labels from physical volume(s).
More information: <https://manned.org/pvremove>.

- Remove a LVM label from a physical volume:

`sudo pvremove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- Display detailed output during the operation:

`sudo pvremove --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- Remove a LVM label without asking for confirmation:

`sudo pvremove --yes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- Forcefully remove a LVM label:

`sudo pvremove --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- Display output in JSON format:

`sudo pvremove --reportformat json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>
