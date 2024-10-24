---
layout: page
title: linux/tuned-adm (English)
description: "Manage and optimize system performance tuning profiles on Linux."
content_hash: c11bfbe104f979298062166eeb32c79309fbc44a
last_modified_at: 2024-10-24
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/tuned-adm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tuned-adm

Manage and optimize system performance tuning profiles on Linux.
More information: <https://tuned-project.org>.

- List available profiles:

`tuned-adm list`

- Show the currently active profile:

`tuned-adm active`

- Set a specific tuning profile:

`tuned-adm profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>

- Recommend a suitable profile based on the current system:

`tuned-adm recommend`

- Disable tuning:

`tuned-adm off`
