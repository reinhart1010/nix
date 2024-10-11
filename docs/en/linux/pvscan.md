---
layout: page
title: linux/pvscan (English)
description: "List all physical volumes and manage their online status."
content_hash: d899e1f46c8c746b1ceb5738cb62387a8427a862
last_modified_at: 2024-10-11
tldri18n_status: 2
---
# pvscan

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
