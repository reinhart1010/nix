---
layout: page
title: common/lerna (한국어)
description: "여러 패키지가 있는 JavaScript 프로젝트 관리."
content_hash: 8877d9d677866fbeeaa43b6b0c2dda4dcbbfd633
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/lerna.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/lerna.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lerna

여러 패키지가 있는 JavaScript 프로젝트 관리.
더 많은 정보: <https://lerna.js.org>.

- 프로젝트 파일 초기화(`lerna.json`, `package.json`, `.git` 등):

`lerna init`

- 각 패키지의 모든 외부 의존성을 설치하고 로컬 의존성을 심볼릭 링크로 연결:

`lerna bootstrap`

- `package.json`에 포함된 특정 스크립트를 모든 패키지에서 실행:

`lerna run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스크립트</span>

- 모든 패키지에서 임의의 셸 명령 실행:

`lerna exec -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>

- 마지막 릴리스 이후 변경된 모든 패키지 배포:

`lerna publish`
