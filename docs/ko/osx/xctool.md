---
layout: page
title: osx/xctool (한국어)
description: "Xcode 프로젝트 빌드."
content_hash: b76ba3c0cbdf5d9351edd54cd7685d3474534515
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/xctool.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/xctool.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/xctool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xctool

Xcode 프로젝트 빌드.
더 많은 정보: <https://github.com/facebookarchive/xctool>.

- 워크스페이스 없이 단일 프로젝트 빌드:

`xctool -project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YourProject.xcodeproj</span>` -scheme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YourScheme</span>` build`

- 워크스페이스의 일부인 프로젝트 빌드:

`xctool -workspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YourWorkspace.xcworkspace</span>` -scheme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YourScheme</span>` build`

- 정리하고, 빌드하고, 모든 테스트 실행:

`xctool -workspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YourWorkspace.xcworkspace</span>` -scheme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YourScheme</span>` clean build test`
