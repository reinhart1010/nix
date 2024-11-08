---
layout: page
title: common/pr (한국어)
description: "파일을 인쇄용으로 페이지화하거나 열로 정렬."
content_hash: adcb35d7219a7ee686a2efc52864793ee1cb5035
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/pr.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pr

파일을 인쇄용으로 페이지화하거나 열로 정렬.
더 많은 정보: <https://www.gnu.org/software/coreutils/pr>.

- 기본 헤더와 푸터로 여러 파일 인쇄:

`pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 사용자 지정 가운데 정렬 헤더로 인쇄:

`pr -h "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">헤더</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 번호가 매겨진 줄과 사용자 지정 날짜 형식으로 인쇄:

`pr -n -D "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">형식</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 모든 파일을 각각 하나의 열에 헤더나 푸터 없이 인쇄:

`pr -m -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 페이지 길이(헤더와 푸터 포함)를 지정하여 페이지 2에서 페이지 5까지 인쇄:

`pr +2:5 -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">페이지_길이</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 각 줄에 대한 오프셋과 잘리는 사용자 지정 페이지 너비로 인쇄:

`pr -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">오프셋</span>` -W `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">너비</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>
