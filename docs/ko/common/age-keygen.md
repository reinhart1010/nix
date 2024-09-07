---
layout: page
title: common/age-keygen (한국어)
description: "`age` 키 쌍을 생성합니다."
content_hash: 000a308b3b899d23c4c92e17c5c9434423e67226
last_modified_at: 2024-09-07
related_topics:
  - title: English version
    url: /en/common/age-keygen.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/age-keygen.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/age-keygen.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/age-keygen.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/age-keygen.html
    icon: bi bi-globe
tldri18n_status: 2
---
# age-keygen

`age` 키 쌍을 생성합니다.
더 보기: 파일을 암호화/복호화하기 위한 `age` 명령어.
더 많은 정보: <https://manned.org/age-keygen>.

- 키 쌍을 생성하고, 암호화되지 않은 파일에 저장한 후 공개키를 `stdout`에 인쇄:

`age-keygen --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 인증 정보(identit[y])를 수신자로 변환하고, 공개 키를 `stdout`에 인쇄:

`age-keygen -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
