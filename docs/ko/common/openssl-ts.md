---
layout: page
title: common/openssl-ts (한국어)
description: "OpenSSL 명령어로 타임스탬프를 생성하고 검증합니다."
content_hash: 304ba52ad08117cf9cb9ee5983de3da763399f60
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/common/openssl-ts.html
    icon: bi bi-globe
tldri18n_status: 2
---
# openssl ts

OpenSSL 명령어로 타임스탬프를 생성하고 검증합니다.
더 많은 정보: <https://www.openssl.org/docs/manmaster/man1/openssl-ts.html>.

- 특정 파일의 SHA-512 타임스탬프 요청을 생성하고 `file.tsq`에 출력:

`openssl ts -query -data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` -sha512 -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.tsq</span>

- 특정 타임스탬프 응답 파일의 날짜 및 메타데이터 확인:

`openssl ts -reply -in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.tsr</span>` -text`

- SSL 인증서 파일을 사용하여 서버로부터 타임스탬프 요청 파일과 타임스탬프 응답 파일 검증:

`openssl ts -verify -in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.tsr</span>` -queryfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.tsq</span>` -partial_chain -CAfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/cert.pem</span>

- 키 및 서명 인증서를 사용하여 요청에 대한 타임스탬프 응답을 생성하고 `file.tsr`에 출력:

`openssl ts -reply -queryfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.tsq</span>` -inkey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/tsakey.pem</span>` -signer tsacert.pem -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.tsr</span>
