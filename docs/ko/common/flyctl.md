---
layout: page
title: common/flyctl (한국어)
description: "flyctl.io용 명령줄 도구."
content_hash: 056ad6eaf61e4e43289a3cc781bee0ea93e55c93
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/flyctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/flyctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># flyctl

flyctl.io용 명령줄 도구.
더 많은 정보: <https://github.com/superfly/flyctl>.

- Fly 계정에 로그인:

`flyctl auth login`

- 특정 Dockerfile에서 애플리케이션을 시작 (기본 경로는 현재 작업 디렉터리):

`flyctl launch --dockerfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/도커파일</span>

- 기본 웹 브라우저에서 현재 배포된 애플리케이션을 열기:

`flyctl open`

- 특정 Dockerfile에서 Fly 애플리케이션을 배포:

`flyctl deploy --dockerfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/도커파일</span>

- 웹 브라우저에서 현재 애플리케이션에 대한 Fly Web UI를 열기:

`flyctl dashboard`

- 로그인한 Fly 계정의 모든 애플리케이션을 나열:

`flyctl apps list`

- 실행 중인 특정 애플리케이션의 상태 보기:

`flyctl status --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_이름</span>

- 버전 정보 표시:

`flyctl version`
