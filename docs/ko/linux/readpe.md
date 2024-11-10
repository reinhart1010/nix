---
layout: page
title: linux/readpe (한국어)
description: "PE 파일에 대한 정보 표시."
content_hash: 8f56b57e6670596a838f09ecb72100a26db5fdb6
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/readpe.html
    icon: bi bi-globe
tldri18n_status: 2
---
# readpe

PE 파일에 대한 정보 표시.
더 많은 정보: <https://manned.org/readpe>.

- PE 파일에 대한 모든 정보 표시:

`readpe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/실행파일</span>

- PE 파일에 존재하는 모든 헤더 표시:

`readpe --all-headers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/실행파일</span>

- PE 파일에 존재하는 모든 섹션 표시:

`readpe --all-sections `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/실행파일</span>

- PE 파일에서 특정 헤더 표시:

`readpe --header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dos|coff|optional</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/실행파일</span>

- 가져온 모든 함수 나열:

`readpe --imports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/실행파일</span>

- 내보낸 모든 함수 나열:

`readpe --exports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/실행파일</span>
