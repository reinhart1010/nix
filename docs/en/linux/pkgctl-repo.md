---
layout: page
title: linux/pkgctl-repo (English)
description: "Manage Git packaging repositories and their configuration for Arch Linux."
content_hash: d8408b0336a852e44db5a7e79a1ac55e6681a0a8
last_modified_at: 2024-09-25
related_topics:
  - title: Nederlands version
    url: /nl/linux/pkgctl-repo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkgctl repo

Manage Git packaging repositories and their configuration for Arch Linux.
See also: `pkgctl`.
More information: <https://manned.org/pkgctl-repo.1>.

- Clone a package repository (requires setting an SSH key in your Arch Linux GitLab account):

`pkgctl repo clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pkgname</span>

- Clone a package repository over HTTPS:

`pkgctl repo clone --protocol=https `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pkgname</span>

- Create a new GitLab package repository and clone it after creation (requires valid GitLab API authentication):

`pkgctl repo create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pkgbase</span>

- Switch a package repository to a specified version:

`pkgctl repo switch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pkgbase</span>

- Open a package repository's website:

`pkgctl repo web `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pkgbase</span>
