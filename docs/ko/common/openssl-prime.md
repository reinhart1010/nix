---
layout: page
title: common/openssl-prime (한국어)
description: "소수를 계산하기 위한 OpenSSL 명령어."
content_hash: ac5a637eca4534f65c9c2aaf36571d03a035d986
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/common/openssl-prime.html
    icon: bi bi-globe
tldri18n_status: 2
---
# openssl prime

소수를 계산하기 위한 OpenSSL 명령어.
더 많은 정보: <https://www.openssl.org/docs/manmaster/man1/openssl-prime.html>.

- 2048비트 소수를 생성하고 16진수로 표시:

`openssl prime -generate -bits 2048 -hex`

- 주어진 숫자가 소수인지 확인:

`openssl prime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>
