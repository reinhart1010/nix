---
layout: page
title: linux/pvs (English)
description: "Display information about physical volumes."
content_hash: d4c2c6434ee28c03c243a39ab08a6e9cf383e73e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pvs

Display information about physical volumes.
See also: `lvm`.
More information: <https://man7.org/linux/man-pages/man8/pvs.8.html>.

- Display information about physical volumes:

`pvs`

- Display non-physical volumes:

`pvs -a`

- Change default display to show more details:

`pvs -v`

- Display only specific fields:

`pvs -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">field_name_1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">field_name_2</span>

- Append field to default display:

`pvs -o +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">field_name</span>

- Suppress heading line:

`pvs --noheadings`

- Use separator to separate fields:

`pvs --separator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">special_character</span>
