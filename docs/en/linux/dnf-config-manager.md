---
layout: page
title: linux/dnf-config-manager (English)
description: "Manage DNF configuration options and repositories on Fedora-based systems."
content_hash: 048169f738e03961e945c225b4d2fffbacdd940b
last_modified_at: 2024-10-09
tldri18n_status: 2
---
# dnf config-manager

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
