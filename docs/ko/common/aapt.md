---
layout: page
title: common/aapt (한국어)
description: "Android Asset Packaging Tool."
content_hash: 2f9c192ef1d77e5b955577fb9a0908f9eae7621b
related_topics:
  - title: Deutsch version
    url: /de/common/aapt.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aapt.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aapt.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aapt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/aapt.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/aapt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aapt.html
    icon: bi bi-globe
---
# aapt

Android Asset Packaging Tool.
안드로이드 앱의 소스를 컴파일하고 패키징합니다.
더 많은 정보: <https://elinux.org/Android_aapt>.

- APK 아카이브에 포함된 파일 나열:

`aapt list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/app.apk</span>

- 앱의 메타데이타 출력 (버전, 권한, 등등...):

`aapt dump badging `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/app.apk</span>

- 지정된 디렉토리에 새 APK 아카이브 생성:

`aapt package -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/app.apk</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉토리/의/경로</span>
