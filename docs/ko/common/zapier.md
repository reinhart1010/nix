---
layout: page
title: common/zapier (한국어)
description: "Zapier 통합을 생성, 자동화 및 관리."
content_hash: 35b3c4c30edc1441d8ab270bf997f0311bcaef98
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/zapier.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zapier.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zapier

Zapier 통합을 생성, 자동화 및 관리.
`build`, `init`, `scaffold`, `push`, `test` 등의 일부 하위 명령에는 자체 사용 설명서가 있습니다.
더 많은 정보: <https://platform.zapier.com/reference/cli>.

- Zapier 계정에 연결:

`zapier login`

- 프로젝트 템플릿으로 새로운 Zapier 통합 초기화:

`zapier init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 시작 트리거, 생성, 검색 또는 리소스를 통합에 추가:

`zapier scaffold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trigger|create|search|resource</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 통합 테스트:

`zapier test`

- Zapier에 통합을 빌드하고 업로드:

`zapier push`

- 도움말 표시:

`zapier help`

- 특정 명령에 대한 도움말 표시:

`zapier help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>
