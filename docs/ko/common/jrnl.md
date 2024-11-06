---
layout: page
title: common/jrnl (한국어)
description: "간단한 커맨드라인 저널 애플리케이션."
content_hash: 9393ffe034334532d4c35ea0facb0864df7a6d2b
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/jrnl.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/jrnl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jrnl

간단한 커맨드라인 저널 애플리케이션.
더 많은 정보: <https://jrnl.sh>.

- 편집기를 사용하여 새 항목 삽입:

`jrnl`

- 빠르게 새 항목 삽입:

`jrnl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">오늘 오전 3시</span>`: `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제목</span>`. `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">내용</span>

- 최근 열 개의 항목 보기:

`jrnl -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- 작년 초부터 올해 3월 초까지 발생한 모든 일 보기:

`jrnl -from "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작년</span>`" -until `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3월</span>

- "texas" 및 "history" 태그가 있는 모든 항목 편집:

`jrnl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@texas</span>` -and `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@history</span>` --edit`
