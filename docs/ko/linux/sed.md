---
layout: page
title: linux/sed (한국어)
description: "스크립트 방식으로 텍스트를 편집합니다."
content_hash: ed32c01b0491235dfac6772a003792a16b53f679
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/sed.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/sed.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/sed.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/sed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sed

스크립트 방식으로 텍스트를 편집합니다.
같이 보기: `awk`, `ed`.
더 많은 정보: <https://www.gnu.org/software/sed/manual/sed.html>.

- 모든 입력 줄에서 `apple` (기본 정규식) 발생 부분을 `mango` (기본 정규식)로 대체하고 결과를 `stdout`에 출력:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed 's/apple/mango/g'`

- 모든 입력 줄에서 `apple` (확장 정규식) 발생 부분을 `APPLE` (확장 정규식)로 대체하고 결과를 `stdout`에 출력:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed -E 's/(apple)/\U\1/g'`

- 특정 파일에서 모든 `apple` (기본 정규식) 발생 부분을 `mango` (기본 정규식)로 대체하고 원본 파일을 직접 덮어쓰기:

`sed -i 's/apple/mango/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 스크립트 [f]파일을 실행하고 결과를 `stdout`에 출력:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.sed</span>

- 첫 번째 줄만 `stdout`에 출력:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed -n '1p'`

- 파일의 첫 번째 줄 [d]삭제:

`sed -i 1d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일의 첫 번째 줄에 새 줄 [i]삽입:

`sed -i '1i\your new line text\' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
