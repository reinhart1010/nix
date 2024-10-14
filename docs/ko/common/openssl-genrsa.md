---
layout: page
title: common/openssl-genrsa (한국어)
description: "RSA 개인 키를 생성하는 OpenSSL 명령어."
content_hash: d3187981c3823170bb922d909494e50958aaad3c
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/common/openssl-genrsa.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/openssl-genrsa.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># openssl genrsa

RSA 개인 키를 생성하는 OpenSSL 명령어.
더 많은 정보: <https://www.openssl.org/docs/manmaster/man1/openssl-genrsa.html>.

- 2048비트 RSA 개인 키를 `stdout`에 생성:

`openssl genrsa`

- 임의 비트 수의 RSA 개인 키를 출력 파일에 저장:

`openssl genrsa -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일.key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>

- RSA 개인 키를 생성하고 AES256으로 암호화 (암호를 입력하라는 메시지가 표시됨):

`openssl genrsa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-aes256</span>
