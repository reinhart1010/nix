---
layout: page
title: linux/uuidd (English)
description: "Daemon for generating UUIDs."
content_hash: 9c851dc6a1a3ea90eb843b7cf392a658ebbe5125
---
# uuidd

Daemon for generating UUIDs.
More information: <https://manned.org/uuidd>.

- Generate a random UUID:

`uuidd --random`

- Generate a bulk number of random UUIDs:

`uuidd --random --uuids `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_uuids</span>

- Generate a time-based UUID, based on the current time and MAC address of the system:

`uuidd --time`
