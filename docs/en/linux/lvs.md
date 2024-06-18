---
layout: page
title: linux/lvs (English)
description: "Display information about logical volumes."
content_hash: 34517a8f83ad8dcc79d90ecad8250d597bdf4ba7
last_modified_at: 2024-06-18
related_topics:
  - title: 中文 version
    url: /zh/linux/lvs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lvs

Display information about logical volumes.
See also: `lvm`.
More information: <https://manned.org/lvs>.

- Display information about logical volumes:

`lvs`

- Display all logical volumes:

`lvs -a`

- Change default display to show more details:

`lvs -v`

- Display only specific fields:

`lvs -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">field_name_1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">field_name_2</span>

- Append field to default display:

`lvs -o +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">field_name</span>

- Suppress heading line:

`lvs --noheadings`

- Use a separator to separate fields:

`lvs --separator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">=</span>
