---
layout: page
title: linux/waitpid (English)
description: "Wait for the termination of arbitrary processes."
content_hash: 2dbb6701ee903456bf2b4a67acefb89f5caf7d52
last_modified_at: 2024-01-23
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/waitpid.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># waitpid

Wait for the termination of arbitrary processes.
See also: `wait`.
More information: <https://manned.org/waitpid.1>.

- Sleep until all processes whose PIDs have been specified have exited:

`waitpid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid1 pid2 ...</span>

- Sleep for at most `n` seconds:

`waitpid --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid1 pid2 ...</span>

- Do not error if specified PIDs have already exited:

`waitpid --exited `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid1 pid2 ...</span>

- Sleep until `n` of the specified processes have exited:

`waitpid --count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid1 pid2 ...</span>

- Display help:

`waitpid -h`
