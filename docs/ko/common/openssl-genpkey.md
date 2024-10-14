---
layout: page
title: common/openssl-genpkey (한국어)
description: "비대칭 키 쌍을 생성하는 OpenSSL 명령어."
content_hash: e7f2bd92dae2a9b3451508865f63823471937f90
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/common/openssl-genpkey.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/openssl-genpkey.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># openssl genpkey

비대칭 키 쌍을 생성하는 OpenSSL 명령어.
더 많은 정보: <https://www.openssl.org/docs/manmaster/man1/openssl-genpkey.html>.

- 2048비트 RSA 개인 키 생성 및 특정 파일에 저장:

`openssl genpkey -algorithm rsa -pkeyopt rsa_keygen_bits:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2048</span>` -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일이름.key</span>

- 곡선 `prime256v1`을 사용하여 타원 곡선 개인 키 생성 및 특정 파일에 저장:

`openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prime256v1</span>` -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일이름.key</span>

- `ED25519` 타원 곡선 개인 키 생성 및 특정 파일에 저장:

`openssl genpkey -algorithm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ED25519</span>` -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일이름.key</span>
