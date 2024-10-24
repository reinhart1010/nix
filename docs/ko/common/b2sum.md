---
layout: page
title: common/b2sum (한국어)
description: "BLACK2 암호화 체크섬을 계산."
content_hash: 19a11b854f9d5bac1a648db65b2293fa8e9469e4
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/common/b2sum.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/b2sum.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/b2sum.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/b2sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/b2sum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# b2sum

BLACK2 암호화 체크섬을 계산.
더 많은 정보: <https://www.gnu.org/software/coreutils/b2sum>.

- 하나 이상의 파일에 대해 BLAKE2 체크섬을 계산:

`b2sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- BLAKE2 체크섬 목록을 계산하고 파일에 저장:

`b2sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.b2</span>

- `stdin`에서 BLAKE2 체크섬을 계산:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | b2sum`

- BLAKE2 합계 및 파일이름의 파일을 읽고 모든 파일에 일치하는 체크섬을 확인:

`b2sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.b2</span>

- 누락된 파일이 있거나 확인에 실패한 경우에만 메시지를 표시:

`b2sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.b2</span>

- 누락된 파일은 무시하고, 확인에 실패한 경우에만 메시지를 표시:

`b2sum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.b2</span>
