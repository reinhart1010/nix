---
layout: page
title: common/pixterm (한국어)
description: "이미지 터미널 출력 도구."
content_hash: 86b03ba5e80f88a1727f41132861f284c7188f9a
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/pixterm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pixterm

이미지 터미널 출력 도구.
같이 보기: `chafa`, `catimg`.
더 많은 정보: <https://github.com/eliukblau/pixterm>.

- 정적 이미지를 터미널에 직접 렌더링:

`pixterm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 이미지의 원본 가로세로 비율 사용:

`pixterm -s 2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 터미널 행 및 열 수를 사용하여 사용자 정의 가로세로 비율 지정:

`pixterm -tr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">24</span>` -tc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 무광 배경색 및 문자 디더링으로 출력 필터링:

`pixterm -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">000000</span>` -d 2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
