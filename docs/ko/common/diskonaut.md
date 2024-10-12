---
layout: page
title: common/diskonaut (한국어)
description: "Rust로 작성된 터미널 디스크 공간 탐색기."
content_hash: 5621bfa7e26cc69b19a98b23612d6be1a41d4946
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/diskonaut.html
    icon: bi bi-globe
tldri18n_status: 2
---
# diskonaut

Rust로 작성된 터미널 디스크 공간 탐색기.
더 많은 정보: <https://github.com/imsnif/diskonaut>.

- 현재 디렉터리에서 `diskonaut`를 시작:

`diskonaut`

- 특정 디렉토리에서 `diskonaut`를 시작:

`diskonaut `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>

- 디스크의 블록 사용량 대신 파일 크기를 표시:

`diskonaut --apparent-size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>

- 삭제 확인 비활성화:

`diskonaut --disable-delete-confirmation`
