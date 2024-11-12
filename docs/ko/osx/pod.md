---
layout: page
title: osx/pod (한국어)
description: "Swift 및 Objective-C Cocoa 프로젝트를 위한 종속성 관리 도구."
content_hash: 59fa829867b020fa87c2fcca2e1207fe2eae201d
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/pod.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/pod.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/pod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pod

Swift 및 Objective-C Cocoa 프로젝트를 위한 종속성 관리 도구.
더 많은 정보: <https://guides.cocoapods.org/terminal/commands.html>.

- 현재 프로젝트에 기본 내용으로 Podfile 생성:

`pod init`

- Podfile에 정의된 모든 포드를 다운로드 및 설치 (이전에 설치되지 않은 경우):

`pod install`

- 사용 가능한 모든 포드 나열:

`pod list`

- 현재 설치된 포드 중 업데이트가 필요한 포드 표시:

`pod outdated`

- 현재 설치된 모든 포드를 최신 버전으로 업데이트:

`pod update`

- 특정 (이전에 설치된) 포드를 최신 버전으로 업데이트:

`pod update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포드_이름</span>

- Xcode 프로젝트에서 CocoaPods 제거:

`pod deintegrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xcode_프로젝트</span>
