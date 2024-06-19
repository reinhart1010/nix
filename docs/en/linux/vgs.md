---
layout: page
title: linux/vgs (English)
description: "Display information about volume groups."
content_hash: 854c52433e6bb93cf215babe4ddb2a4df0485908
last_modified_at: 2024-06-19
tldri18n_status: 2
---
# vgs

Display information about volume groups.
See also: `lvm`.
More information: <https://manned.org/vgs>.

- Display information about volume groups:

`vgs`

- Display all volume groups:

`vgs -a`

- Change default display to show more details:

`vgs -v`

- Display only specific fields:

`vgs -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">field_name_1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">field_name_2</span>

- Append field to default display:

`vgs -o +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">field_name</span>

- Suppress heading line:

`vgs --noheadings`

- Use separator to separate fields:

`vgs --separator =`
