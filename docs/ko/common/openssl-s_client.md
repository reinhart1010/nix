---
layout: page
title: common/openssl-s_client (한국어)
description: "TLS 클라이언트 연결을 생성하는 OpenSSL 명령어."
content_hash: 26709e8d7468407211ff7ae1ea38508036cffa56
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/common/openssl-s_client.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/openssl-s_client.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># openssl s_client

TLS 클라이언트 연결을 생성하는 OpenSSL 명령어.
더 많은 정보: <https://www.openssl.org/docs/manmaster/man1/openssl-s_client.html>.

- 도메인 인증서의 시작 및 만료 날짜 표시:

`openssl s_client -connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` 2>/dev/null | openssl x509 -noout -dates`

- SSL/TLS 서버에서 제공하는 인증서 표시:

`openssl s_client -connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` </dev/null`

- SSL/TLS 서버에 연결할 때 서버 이름 지시자(SNI) 설정:

`openssl s_client -connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` -servername `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>

- HTTPS 서버의 전체 인증서 체인 표시:

`openssl s_client -connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>`:443 -showcerts </dev/null`
