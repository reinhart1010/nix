---
layout: page
title: linux/vgs (English)
description: "Display information about volume groups."
content_hash: 06a4a09b69a145070f27193e7bfc0e1c965de897
---
# vgs

Display information about volume groups.
See also: `lvm`.
More information: <https://man7.org/linux/man-pages/man8/vgs.8.html>.

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
