---
layout: page
title: linux/kpartx (English)
description: "Create device maps from partition tables."
content_hash: 60529a918e8e0638c235f8056a69e8a53913d5f9
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# kpartx

Create device maps from partition tables.
More information: <https://manned.org/kpartx>.

- Add partition mappings:

`kpartx -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">whole_disk.img</span>

- Delete partition mappings:

`kpartx -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">whole_disk.img</span>

- List partition mappings:

`kpartx -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">whole_disk.img</span>
