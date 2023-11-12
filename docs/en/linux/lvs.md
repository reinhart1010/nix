---
layout: page
title: linux/lvs (English)
description: "Display information about logical volumes."
content_hash: ee398243cb9d6603bf2cc5ea53de18f034a2f7b3
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/linux/lvs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lvs

Display information about logical volumes.
See also: `lvm`.
More information: <https://man7.org/linux/man-pages/man8/lvs.8.html>.

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
