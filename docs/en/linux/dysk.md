---
layout: page
title: linux/dysk (English)
description: "Display filesystem information in a table."
content_hash: 0ef557a0629d143f80345836632cf3afde6e1b6d
last_modified_at: 2024-08-08
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dysk.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dysk

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
