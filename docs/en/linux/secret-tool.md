---
layout: page
title: linux/secret-tool (English)
description: "Store and retrieve passwords, part of the `libsecret` package."
content_hash: c4629dd49a5c593ad3828d3bab6a1df9cedc3078
last_modified_at: 2024-09-26
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/secret-tool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># secret-tool

Store and retrieve passwords, part of the `libsecret` package.
Communicates with Freedesktop secret service implementations such as `gnome-keyring`.
More information: <https://gnome.pages.gitlab.gnome.org/libsecret/>.

- Store a secret with an optional label:

`secret-tool store --label=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Retrieve a secret:

`secret-tool lookup key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>

- Get more information about a secret:

`secret-tool search key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>

- Delete a stored secret:

`secret-tool clear key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>
