---
layout: page
title: common/openssl-x509 (한국어)
description: "X.509 인증서를 관리하기 위한 OpenSSL 명령어."
content_hash: cc868a58102c346d8b26e6a5dc1df740a71796ec
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/common/openssl-x509.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/openssl-x509.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># openssl x509

X.509 인증서를 관리하기 위한 OpenSSL 명령어.
더 많은 정보: <https://www.openssl.org/docs/manmaster/man1/openssl-x509.html>.

- 인증서 정보 표시:

`openssl x509 -in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일이름.crt</span>` -noout -text`

- 인증서 만료 날짜 표시:

`openssl x509 -enddate -noout -in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일이름.pem</span>

- 인증서를 이진 DER 인코딩과 텍스트 PEM 인코딩 간 변환:

`openssl x509 -inform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">der</span>` -outform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pem</span>` -in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원본_인증서_파일</span>` -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변환된_인증서_파일</span>

- 인증서의 공개 키를 파일에 저장:

`openssl x509 -in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인증서_파일</span>` -noout -pubkey -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일</span>
