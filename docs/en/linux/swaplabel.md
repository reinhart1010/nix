---
layout: page
title: linux/swaplabel (English)
description: "Print or change the label or UUID of a swap area."
content_hash: 56ed4c2bdef31c45543a0f12b99d109812b92e13
last_modified_at: 2023-07-09
---
# swaplabel

Print or change the label or UUID of a swap area.
Note: `path/to/file` can either point to a regular file or a swap partition.
More information: <https://manned.org/swaplabel>.

- Display the current label and UUID of a swap area:

`swaplabel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Set the label of a swap area:

`swaplabel --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_label</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Set the UUID of a swap area (you can generate a UUID using `uuidgen`):

`swaplabel --uuid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_uuid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
