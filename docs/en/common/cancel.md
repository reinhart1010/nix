---
layout: page
title: common/cancel (English)
description: "Cancel print jobs."
content_hash: 46f5dc846a2006088149f4d5168495e2baec0e02
last_modified_at: 2024-02-19
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/cancel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cancel

Cancel print jobs.
See also: `lp`, `lpmove`, `lpstat`.
More information: <https://openprinting.github.io/cups/doc/man-cancel.html>.

- Cancel the current job of the default printer (set with `lpoptions -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer</span>):

`cancel`

- Cancel the jobs of the default printer owned by a specific [u]ser:

`cancel -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Cancel the current job of a specific printer:

`cancel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer</span>

- Cancel a specific job from a specific printer:

`cancel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>

- Cancel [a]ll jobs of all printers:

`cancel -a`

- Cancel [a]ll jobs of a specific printer:

`cancel -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer</span>

- Cancel the current job of a specific server and then delete ([x]) job data files:

`cancel -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>` -x`
