---
layout: page
title: linux/disown (English)
description: "Allow sub-processes to live beyond the shell that they are attached to."
content_hash: 6a4230d1438870249e2e74c235a5491a85e5bfb6
last_modified_at: 2023-11-12
related_topics:
  - title: हिन्दी version
    url: /hi/linux/disown.html
    icon: bi bi-globe
tldri18n_status: 2
---
# disown

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
