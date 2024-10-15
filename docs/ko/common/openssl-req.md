---
layout: page
title: common/openssl-req (한국어)
description: "PKCS#10 인증서 서명 요청을 관리하는 OpenSSL 명령어."
content_hash: 87d3452ce85982a0a5a81875cb03ebf084e08dc1
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/common/openssl-req.html
    icon: bi bi-globe
tldri18n_status: 2
---
# openssl req

PKCS#10 인증서 서명 요청을 관리하는 OpenSSL 명령어.
더 많은 정보: <https://www.openssl.org/docs/manmaster/man1/openssl-req.html>.

- 인증 기관에 보낼 인증서 서명 요청 생성:

`openssl req -new -sha256 -key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일이름.key</span>` -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일이름.csr</span>

- 자체 서명된 인증서와 해당 키 쌍을 생성하여 파일에 저장:

`openssl req -new -x509 -newkey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rsa</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4096</span>` -keyout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일이름.key</span>` -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일이름.cert</span>` -subj "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/C=XX/CN=foobar</span>`" -days `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">365</span>
