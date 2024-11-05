---
layout: page
title: common/ng (한국어)
description: "Angular 애플리케이션 생성 및 관리 도구."
content_hash: 0910858a8db474c1a82d50c7c9cfc406d149edec
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/ng.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/ng.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ng.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ng

Angular 애플리케이션 생성 및 관리 도구.
더 많은 정보: <https://angular.io/cli>.

- 디렉토리 내에 새로운 Angular 애플리케이션 생성:

`ng new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>

- 애플리케이션에 새 컴포넌트 추가:

`ng generate component `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컴포넌트_이름</span>

- 애플리케이션에 새 클래스 추가:

`ng generate class `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클래스_이름</span>

- 애플리케이션에 새 디렉티브 추가:

`ng generate directive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉티브_이름</span>

- 루트 디렉토리에서 애플리케이션 실행:

`ng serve`

- 애플리케이션 빌드:

`ng build`

- 유닛 테스트 실행:

`ng test`

- 현재 Angular 설치 버전 표시:

`ng version`
