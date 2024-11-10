---
layout: page
title: linux/mcookie (한국어)
description: "랜덤 128비트 16진수 숫자를 생성합니다."
content_hash: fe5830f9e71d32375344cfcbd3f23bc0f411bde0
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/mcookie.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mcookie

랜덤 128비트 16진수 숫자를 생성합니다.
더 많은 정보: <https://manned.org/mcookie>.

- 랜덤 숫자 생성:

`mcookie`

- 파일의 내용을 난수 생성의 시드로 사용하여 랜덤 숫자 생성:

`mcookie --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일에서 특정 바이트 수를 난수 생성의 시드로 사용하여 랜덤 숫자 생성:

`mcookie --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` --max-size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">바이트_수</span>

- 사용된 난수의 출처 및 시드와 같은 세부 정보를 출력:

`mcookie --verbose`
