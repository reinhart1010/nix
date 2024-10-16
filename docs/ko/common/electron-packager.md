---
layout: page
title: common/electron-packager (한국어)
description: "Windows, Linux 및 macOS용 Electron 앱 실행 파일을 빌드."
content_hash: 36eccdce41b2ab75f3fa1bec483d2e6361d94336
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/electron-packager.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/electron-packager.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># electron-packager

Windows, Linux 및 macOS용 Electron 앱 실행 파일을 빌드.
애플리케이션 디렉터리에 유효한 package.json이 필요.
더 많은 정보: <https://github.com/electron/electron-packager>.

- 현재 아키텍처 및 플랫폼에 대한 애플리케이션을 패키징:

`electron-packager "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/앱</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션</span>`"`

- 모든 아키텍처와 플랫폼에 대한 애플리케이션을 패키징:

`electron-packager "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/앱</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션</span>`" --all`

- 64비트 Linux용 애플리케이션을 패키징:

`electron-packager "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/앱</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션</span>`" --platform="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linux</span>`" --arch="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x64</span>`"`

- ARM macOS용 애플리케이션을 패키징:

`electron-packager "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/앱</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션</span>`" --platform="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">darwin</span>`" --arch="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arm64</span>`"`
