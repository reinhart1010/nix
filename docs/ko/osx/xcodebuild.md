---
layout: page
title: osx/xcodebuild (한국어)
description: "Xcode 프로젝트 빌드."
content_hash: 542f5f8028756671b714be596d5938655ae35b3a
last_modified_at: 2024-10-24
related_topics:
  - title: English version
    url: /en/osx/xcodebuild.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/xcodebuild.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/xcodebuild.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/xcodebuild.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xcodebuild

Xcode 프로젝트 빌드.
더 많은 정보: <https://developer.apple.com/library/archive/technotes/tn2339/_index.html>.

- 워크스페이스 빌드:

`xcodebuild -workspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">워크스페이스_이름.workspace</span>` -scheme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스킴_이름</span>` -configuration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_이름</span>` clean build SYMROOT=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SYMROOT_경로</span>

- 프로젝트 빌드:

`xcodebuild -target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_이름</span>` -configuration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_이름</span>` clean build SYMROOT=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SYMROOT_경로</span>

- SDK 표시:

`xcodebuild -showsdks`
