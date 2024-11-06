---
layout: page
title: common/xxd (한국어)
description: "바이너리 파일에서 16진수 표현(hexdump)을 생성하거나 그 반대로 변환."
content_hash: 7d3bea57a6a8394448d7f402058ec00e4be753b7
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/xxd.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/xxd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xxd

바이너리 파일에서 16진수 표현(hexdump)을 생성하거나 그 반대로 변환.
더 많은 정보: <https://manned.org/xxd>.

- 바이너리 파일에서 16진수 덤프 생성 및 출력 표시:

`xxd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일</span>

- 바이너리 파일에서 16진수 덤프를 생성하고 텍스트 파일로 저장:

`xxd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일</span>

- 연속된 0이 있을 경우 별표로 대체하여 더 간결한 출력 표시:

`xxd -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일</span>

- 각 1옥텟(바이트)로 이루어진 10개의 열로 출력 표시:

`xxd -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일</span>

- 최대 32바이트 길이까지만 출력 표시:

`xxd -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">32</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일</span>

- 열 사이에 간격 없이 평문 모드로 출력 표시:

`xxd -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일</span>

- 평문 16진수 덤프를 바이너리로 복원하고 바이너리 파일로 저장:

`xxd -r -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일</span>
