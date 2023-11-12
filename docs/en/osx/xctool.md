---
layout: page
title: osx/xctool (English)
description: "Tool for building Xcode projects."
content_hash: c2dc20e30acdf16dca4f2a6421c01369ad50939a
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/osx/xctool.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/xctool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xctool

Tool for building Xcode projects.
More information: <https://github.com/facebookarchive/xctool>.

- Build a single project without any workspace:

`xctool -project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YourProject.xcodeproj</span>` -scheme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YourScheme</span>` build`

- Build a project that is part of a workspace:

`xctool -workspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YourWorkspace.xcworkspace</span>` -scheme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YourScheme</span>` build`

- Clean, build and execute all the tests:

`xctool -workspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YourWorkspace.xcworkspace</span>` -scheme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YourScheme</span>` clean build test`
