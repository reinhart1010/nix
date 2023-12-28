---
layout: page
title: common/lprm (English)
description: "Cancel queued print jobs of a server."
content_hash: ed6c0d55d723d821bcc67f8cd4928a3eb44a6cf7
last_modified_at: 2023-12-28
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/lprm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lprm

Cancel queued print jobs of a server.
See also: `lpq`.
More information: <https://openprinting.github.io/cups/doc/man-lprm.html>.

- Cancel current job on the default printer:

`lprm`

- Cancel a job of a specific server:

`lprm -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server[:port]</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>

- Cancel multiple jobs with a encrypted connection to the server:

`lprm -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id1 job_id2 ...</span>

- Cancel all jobs:

`lprm -`

- Cancel the current job of a specific printer or class:

`lprm -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination[/instance]</span>
