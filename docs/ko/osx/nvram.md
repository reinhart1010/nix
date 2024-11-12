---
layout: page
title: osx/nvram (한국어)
description: "펌웨어 변수를 조작합니다."
content_hash: 1a6350221b149fb628baec82fed58f3078ae8595
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/nvram.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/nvram.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nvram

펌웨어 변수를 조작합니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/nvram.8.html>.

- NVRAM에 저장된 모든 변수 [p]출력:

`nvram -p`

- NVRAM에 저장된 모든 변수를 [x]ML 형식으로 [p]출력:

`nvram -xp`

- 펌웨어 변수의 값 수정:

`sudo nvram `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>`"`

- 펌웨어 변수 [d]삭제:

`sudo nvram -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 모든 펌웨어 변수 [c]지우기:

`sudo nvram -c`

- 특정 [x]ML [f]파일에서 펌웨어 변수 설정:

`sudo nvram -xf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.xml</span>
