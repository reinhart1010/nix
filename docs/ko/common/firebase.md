---
layout: page
title: common/firebase (한국어)
description: "Firebase 프로젝트를 테스트, 관리, 배포."
content_hash: b1d59bc9fb53e1956ec771eccb057f855099ceaf
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/firebase.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/firebase.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># firebase

Firebase 프로젝트를 테스트, 관리, 배포.
더 많은 정보: <https://github.com/firebase/firebase-tools>.

- <https://console.firebase.google.com>에 로그인:

`firebase login`

- 기존 Firebase 프로젝트 나열:

`firebase projects:list`

- 대화형 마법사를 시작하여 현재 디렉터리에 Firebase 프로젝트를 만듬:

`firebase init`

- 현재 Firebase 프로젝트에 코드와 리소스를 배포:

`firebase deploy`

- 현재 Firebase 프로젝트의 리소스를 정적으로 호스팅하기 위해 로컬 서버를 시작:

`firebase serve`

- 대화형 마법사를 시작하여 기본 웹 브라우저에서 현재 Firebase 프로젝트의 여러 링크 중 하나를 열기:

`firebase open`
