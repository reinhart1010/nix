---
layout: page
title: linux/pvscan (English)
description: "List all physical volumes and manage their online status."
content_hash: d899e1f46c8c746b1ceb5738cb62387a8427a862
last_modified_at: 2024-10-10
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pvscan.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pvscan

List all physical volumes and manage their online status.
More information: <https://manned.org/pvscan>.

- List all physical volumes:

`pvscan`

- Show the volume group that uses a specific physical volume:

`pvscan --cache --listvg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Show logical volumes that use a specific physical volume:

`pvscan --cache --listlvs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Display detailed information in JSON format:

`pvscan --reportformat json`
