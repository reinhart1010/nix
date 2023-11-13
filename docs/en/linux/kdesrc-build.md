---
layout: page
title: linux/kdesrc-build (English)
description: "Easily build KDE components from its source repositories."
content_hash: bb2b57edd6ec514f5963ac1518a2ce3157d08619
last_modified_at: 2023-11-13
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/kdesrc-build.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kdesrc-build

Easily build KDE components from its source repositories.
More information: <https://invent.kde.org/sdk/kdesrc-build>.

- Initialize kdesrc-build:

`kdesrc-build --initial-setup`

- Build a KDE `component_name` and its dependencies from source:

`kdesrc-build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">component_name</span>

- Build a component without updating its local code and without compiling its dependencies:

`kdesrc-build --no-src --no-include-dependencies `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">component_name</span>

- Refresh the build directories:

`kdesrc-build --refresh-build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">component_name</span>
