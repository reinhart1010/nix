---
layout: page
title: osx/xctool (English)
description: "Tool for building Xcode projects."
content_hash: 99f189dd911c39de2e95b7727fdd04910b5222dc
related_topics:
  - title: 中文 version
    url: /zh/osx/xctool.html
    icon: bi bi-globe
---
# xctool

Tool for building Xcode projects.
More information: <https://github.com/facebook/xctool>.

- Build a single project without any workspace:

`xctool -project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YourProject.xcodeproj</span>` -scheme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YourScheme</span>` build`

- Build a project that is part of a workspace:

`xctool -workspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YourWorkspace.xcworkspace</span>` -scheme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YourScheme</span>` build`

- Clean, build and execute all the tests:

`xctool -workspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YourWorkspace.xcworkspace</span>` -scheme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YourScheme</span>` clean build test`
