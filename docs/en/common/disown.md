---
layout: page
title: common/disown (English)
description: "Allow sub-processes to live beyond the shell that they are attached to."
content_hash: 6a4230d1438870249e2e74c235a5491a85e5bfb6
last_modified_at: 2024-10-07
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/disown.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># disown

Allow sub-processes to live beyond the shell that they are attached to.
See also the `jobs` command.
More information: <https://www.gnu.org/software/bash/manual/bash.html#index-disown>.

- Disown the current job:

`disown`

- Disown a specific job:

`disown %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_number</span>

- Disown all jobs:

`disown -a`

- Keep job (do not disown it), but mark it so that no future SIGHUP is received on shell exit:

`disown -h %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_number</span>
