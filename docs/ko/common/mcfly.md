---
layout: page
title: common/mcfly (한국어)
description: "스마트 명령어 기록 검색 및 관리 도구."
content_hash: 7c662962dc23e30f6c9333550061fd91970cda2e
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/mcfly.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mcfly.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mcfly

스마트 명령어 기록 검색 및 관리 도구.
기본 셸 히스토리 검색(CTRL-R)을 대체하여 명령어에 대한 문맥과 관련성을 제공하는 지능형 검색 엔진.
더 많은 정보: <https://github.com/cantino/mcfly>.

- 지정된 셸에 대한 mcfly 통합 코드 출력:

`mcfly init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|fish|zsh</span>

- 기록에서 명령어를 검색하여 20개의 결과 출력:

`mcfly search --results `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색어</span>`"`

- 새로운 명령어를 기록에 추가:

`mcfly add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>`"`

- 디렉토리가 이동되었음을 기록하고, 이전 경로의 기록을 새로운 경로로 전송:

`mcfly move "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이전_폴더</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새로운_폴더</span>`"`

- 추천 엔진 훈련 (개발자 도구):

`mcfly train`

- 특정 하위 명령어에 대한 도움말 표시:

`mcfly help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위_명령어</span>
