---
layout: page
title: linux/aurpublish (English)
description: "Publish Arch User Repository packages."
content_hash: c72d77c6cd77f5dfb3fcbca8113a0ceefdd01dd4
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/linux/aurpublish.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aurpublish

Publish Arch User Repository packages.
More information: <https://github.com/eli-schwartz/aurpublish>.

- Verify `PKGBUILD` integrity, generate `.SRCINFO`, create a commit message template, and publish the package to the AUR:

`aurpublish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Add githooks to the current repository:

`aurpublish setup`
