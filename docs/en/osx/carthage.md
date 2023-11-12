---
layout: page
title: osx/carthage (English)
description: "A dependency management tool for Cocoa applications."
content_hash: a47c10e12ab10be7fa34dd84bf91c10622d45591
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/osx/carthage.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/carthage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# carthage

A dependency management tool for Cocoa applications.
More information: <https://github.com/Carthage/Carthage>.

- Download the latest version of all dependencies mentioned in Cartfile, and build them:

`carthage update`

- Update dependencies, but only build for iOS:

`carthage update --platform ios`

- Update dependencies, but don't build any of them:

`carthage update --no-build`

- Download and rebuild the current version of dependencies (without updating them):

`carthage bootstrap`

- Rebuild a specific dependency:

`carthage build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependency</span>
