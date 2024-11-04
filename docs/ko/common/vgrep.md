---
layout: page
title: common/vgrep (한국어)
description: "사용하기 쉬운 grep용 페이지 도구."
content_hash: c09866c2cbc1f10658de7b44937174064e66434f
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/vgrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vgrep

사용하기 쉬운 grep용 페이지 도구.
같이 보기: `ugrep`, `rg`.
더 많은 정보: <https://github.com/vrothberg/vgrep>.

- 현재 디렉토리에서 패턴을 재귀적으로 검색하고 캐시:

`vgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>

- 캐시된 내용 표시:

`vgrep`

- 기본 편집기로 캐시에서 "4번째" 일치 항목 열기:

`vgrep --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- 캐시에서 각 일치 항목에 대해 "3" 줄의 컨텍스트 표시:

`vgrep --show=context`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- 트리 내 각 디렉토리에 대한 일치 항목 수 표시:

`vgrep --show=tree`

- 트리 내 각 파일에 대한 일치 항목 수 표시:

`vgrep --show=files`

- 캐시된 일치 항목과 함께 대화형 셸 시작:

`vgrep --interactive`
