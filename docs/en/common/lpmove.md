---
layout: page
title: common/lpmove (English)
description: "Move a job or all jobs to another printer."
content_hash: 3773832ce387a74ea242e0fbf5569193ca053b9d
last_modified_at: 2023-12-28
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/lpmove.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lpmove

Move a job or all jobs to another printer.
See also: `cancel`, `lp`, `lpr`, `lprm`.
More information: <https://openprinting.github.io/cups/doc/man-lpmove.html>.

- Move a specific job to `new_printer`:

`lpmove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_printer</span>

- Move a job from `old_printer` to `new_printer`:

`lpmove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old_printer</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_printer</span>

- Move all jobs from `old_printer` to `new_printer`:

`lpmove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old_printer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_printer</span>

- Move a specific job to `new_printer` on a specific server:

`lpmove -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_printer</span>
