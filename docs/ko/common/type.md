---
layout: page
title: common/type (한국어)
description: "셀이 실행할 명령의 유형을 표시합니다."
content_hash: 3f799008f9d5a21f0cc69c4ed39b98417b0e8237
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/type.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/type.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/type.html
    icon: bi bi-globe
tldri18n_status: 2
---
# type

셀이 실행할 명령의 유형을 표시합니다.
참고: 모든 예시는 POSIX 호환이 아닙니다.
더 많은 정보: <https://manned.org/type>.

- 명령의 유형 표시:

`type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 지정된 실행 파일을 포함하는 모든 위치 표시 (Bash/fish/Zsh 셸에서만 작동):

`type -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 실행될 디스크 파일의 이름 표시 (Bash/fish/Zsh 셸에서만 작동):

`type -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 특정 명령, 별칭/키워드/함수/내장 명령/파일의 유형 표시 (Bash/fish 셸에서만 작동):

`type -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>
