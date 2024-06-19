---
layout: page
title: linux/pvs (English)
description: "Display information about physical volumes."
content_hash: 0a9a54e9fcb23e6a0ae0be84324a99570b25ee82
last_modified_at: 2024-06-19
tldri18n_status: 2
---
# pvs

Display information about physical volumes.
See also: `lvm`.
More information: <https://manned.org/pvs>.

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
