---
layout: page
title: common/shred (한국어)
description: "파일을 덮어써서 데이터를 안전하게 삭제."
content_hash: 582aac220d319d42ab0ca983eef21d1dabaa30e5
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/shred.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/shred.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shred

파일을 덮어써서 데이터를 안전하게 삭제.
더 많은 정보: <https://www.gnu.org/software/coreutils/shred>.

- 파일 덮어쓰기:

`shred `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일을 덮어쓰고 진행 상황 표시:

`shred --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일을 덮어쓰고 무작위 데이터 대신 [z]ero(0)로 남기기:

`shred --zero `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일을 특정 횟수[n]만큼 덮어쓰기:

`shred --iterations `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">25</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일을 덮어쓰고 삭제:

`shred --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일을 100번 덮어쓰고 마지막에 [z]ero(0)로 덮어쓰기 추가, 덮어쓰기 후 파일 삭제 및 진행 상황을 화면에 [v]자세히 표시:

`shred -vzun 100 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
