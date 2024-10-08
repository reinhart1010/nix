---
layout: page
title: linux/dnf-config-manager (English)
description: "Manage DNF configuration options and repositories on Fedora-based systems."
content_hash: 048169f738e03961e945c225b4d2fffbacdd940b
last_modified_at: 2024-10-08
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dnf-config-manager.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dnf config-manager

Manage DNF configuration options and repositories on Fedora-based systems.
More information: <https://manned.org/dnf-config-manager>.

- Add (and enable) a repository from a URL:

`dnf config-manager --add-repo=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_url</span>

- Print current configuration values:

`dnf config-manager --dump`

- Enable a specific repository:

`dnf config-manager --set-enabled `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_id</span>

- Disable specified repositories:

`dnf config-manager --set-disabled `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_id1 repository_id2 ...</span>

- Set a configuration option for a repository:

`dnf config-manager --setopt=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">option</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Display help:

`dnf config-manager --help-cmd`
