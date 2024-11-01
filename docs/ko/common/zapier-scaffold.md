---
layout: page
title: common/zapier-scaffold (한국어)
description: "통합에 시작 트리거, 생성, 검색 또는 리소스를 추가합니다."
content_hash: 749cd327744aa416895e97b4d12ea5408ecbd218
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/zapier-scaffold.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zapier-scaffold.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zapier scaffold

통합에 시작 트리거, 생성, 검색 또는 리소스를 추가합니다.
더 많은 정보: <https://platform.zapier.com/reference/cli#scaffold>.

- 새 트리거, 생성, 검색 또는 리소스 스캐폴드:

`zapier scaffold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trigger|search|create|resource</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명사</span>

- 스캐폴드된 파일의 사용자 지정 대상 폴더 지정:

`zapier scaffold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trigger|search|create|resource</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명사</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--dest</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 스캐폴딩 시 기존 파일 덮어쓰기:

`zapier scaffold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trigger|search|create|resource</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명사</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--force</span>

- 스캐폴드된 파일에서 주석 제외:

`zapier scaffold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trigger|search|create|resource</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명사</span>` --no-help`

- 추가 디버깅 출력 표시:

`zapier scaffold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--debug</span>
