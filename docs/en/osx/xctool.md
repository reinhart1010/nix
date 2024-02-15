---
layout: page
title: osx/xctool (English)
description: "Build Xcode projects."
content_hash: 66c0e9a1071225c3f4f0c12cbe3f76a0c1622e91
last_modified_at: 2024-02-15
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

Build Xcode projects.
More information: <https://github.com/facebookarchive/xctool>.

- Build a single project without any workspace:

`xctool -project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YourProject.xcodeproj</span>` -scheme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YourScheme</span>` build`

- Build a project that is part of a workspace:

`xctool -workspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YourWorkspace.xcworkspace</span>` -scheme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YourScheme</span>` build`

- Clean, build and execute all the tests:

`xctool -workspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YourWorkspace.xcworkspace</span>` -scheme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YourScheme</span>` clean build test`
