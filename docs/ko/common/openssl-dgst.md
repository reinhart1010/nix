---
layout: page
title: common/openssl-dgst (한국어)
description: "OpenSSL 명령어로, 메시지 다이제스트 값을 생성하고 서명 작업을 수행합니다."
content_hash: be6fcc2f01458431d0677c02e7b15a46b4230669
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/common/openssl-dgst.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/openssl-dgst.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># openssl dgst

OpenSSL 명령어로, 메시지 다이제스트 값을 생성하고 서명 작업을 수행합니다.
더 많은 정보: <https://www.openssl.org/docs/manmaster/man1/openssl-dgst.html>.

- 파일의 SHA256 다이제스트 값을 계산하여 특정 파일에 저장:

`openssl dgst -sha256 -binary -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일</span>

- RSA 키를 사용하여 파일에 서명하고 결과를 특정 파일에 저장:

`openssl dgst -sign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">개인_키_파일</span>` -sha256 -sigopt rsa_padding_mode:pss -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일</span>

- RSA 서명 검증:

`openssl dgst -verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">공개_키_파일</span>` -signature `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서명_파일</span>` -sigopt rsa_padding_mode:pss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서명_메시지_파일</span>

- ECDSA 키를 사용하여 파일에 서명:

`openssl dgst -sign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">개인_키_파일</span>` -sha256 -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일</span>

- ECDSA 서명 검증:

`openssl dgst -verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">공개_키_파일</span>` -signature `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서명_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서명_메시지_파일</span>
