---
layout: page
title: linux/getent (English)
description: "Get entries from Name Service Switch libraries."
content_hash: 95e0f913c8978ed706c13ec04a5300eeba660796
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# getent

Get entries from Name Service Switch libraries.
More information: <https://manned.org/getent>.

- Get list of all groups:

`getent group`

- See the members of a group:

`getent group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>

- Get list of all services:

`getent services`

- Find a username by UID:

`getent passwd 1000`

- Perform a reverse DNS lookup:

`getent hosts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>
