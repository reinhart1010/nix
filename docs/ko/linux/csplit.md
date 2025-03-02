---
layout: page
title: linux/csplit (한국어)
description: "파일을 여러 조각으로 분할합니다."
content_hash: c7ee7d48a5c96d1d63d66c35489adeb34142d16c
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/csplit.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/csplit.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/csplit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# csplit

파일을 여러 조각으로 분할합니다.
"xx00", "xx01" 등의 이름으로 파일을 생성합니다.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/csplit-invocation.html>.

- 파일을 5번째 및 23번째 줄에서 분할:

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` 5 23`

- 파일을 5줄마다 분할 (총 줄 수가 5로 나누어 떨어지지 않으면 실패):

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` 5 {*}`

- 정확한 나누기 오류를 무시하고 파일을 5줄마다 분할:

`csplit -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` 5 {*}`

- 5번째 줄에서 파일을 분할하고 출력 파일에 사용자 지정 접두사를 사용:

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` 5 -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">접두사</span>

- 정규 표현식과 일치하는 줄에서 파일을 분할:

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` /`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`/`
