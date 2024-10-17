---
layout: page
title: common/envsubst (한국어)
description: "환경변수를 쉘 형식 문자열의 값으로 대체."
content_hash: 850b32d73c4e24209d066437136e60fdf46e5ea5
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/envsubst.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/envsubst.html
    icon: bi bi-globe
tldri18n_status: 2
---
# envsubst

환경변수를 쉘 형식 문자열의 값으로 대체.
교체할 변수는 `${var}` 또는 `$var` 형식이어야 함.
더 많은 정보: <https://www.gnu.org/software/gettext/manual/html_node/envsubst-Invocation.html>.

- `stdin`의 환경 변수를 바꾸고 `stdout`으로 출력:

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$HOME</span>`' | envsubst`

- 입력 파일의 환경 변수를 바꾸고 `stdout`으로 출력:

`envsubst < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>

- 입력 파일의 환경 변수를 바꾸고 파일로 출력:

`envsubst < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- 공백으로 구분된 목록에서 입력 파일의 환경 변수를 변경:

`envsubst '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$USER $SHELL $HOME</span>`' < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>
