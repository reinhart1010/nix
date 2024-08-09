---
layout: page
title: linux/dysk (English)
description: "Display filesystem information in a table."
content_hash: 0ef557a0629d143f80345836632cf3afde6e1b6d
last_modified_at: 2024-08-09
tldri18n_status: 2
---
# dysk

Display filesystem information in a table.
More information: <https://dystroy.org/dysk>.

- Get a standard overview of your usual disks:

`dysk`

- Sort by free size:

`dysk --sort free`

- Include only HDD disks:

`dysk --filter 'disk = HDD'`

- Exclude SSD disks:

`dysk --filter 'disk <> SSD'`

- Display disks with high utilization or low free space:

`dysk --filter 'use > 65% | free < 50G'`
