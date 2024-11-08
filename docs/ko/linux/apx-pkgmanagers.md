---
layout: page
title: linux/apx-pkgmanagers (한국어)
description: "`apx`에서 패키지 관리자를 관리합니다."
content_hash: ef5f2fd7f5913560433f363e5a2abe8417ca1aea
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/apx-pkgmanagers.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apx-pkgmanagers.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/apx-pkgmanagers.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># apx pkgmanagers

`apx`에서 패키지 관리자를 관리합니다.
참고: 사용자가 생성한 패키지 관리자 구성은 `~/.local/share/apx/pkgmanagers`에 저장됩니다.
더 많은 정보: <https://github.com/Vanilla-OS/apx>.

- 새 패키지 관리자 구성을 대화형으로 생성:

`apx pkgmanagers create`

- 사용 가능한 모든 패키지 관리자 구성 나열:

`apx pkgmanagers list`

- 패키지 관리자 구성 제거:

`apx pkgmanagers rm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>

- 특정 패키지 관리자에 대한 정보 표시:

`apx pkgmanagers show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>
