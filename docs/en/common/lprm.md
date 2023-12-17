---
layout: page
title: common/lprm (English)
description: "Cancel queued print jobs of a server."
content_hash: 6ad67900fc44ff9875336be031f4f2940da3159d
last_modified_at: 2023-12-17
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/lprm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lprm

Cancel queued print jobs of a server.
See also: `lpq`.
More information: <https://www.cups.org/doc/man-lprm.html>.

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
