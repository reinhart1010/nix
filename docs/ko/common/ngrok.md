---
layout: page
title: common/ngrok (한국어)
description: "로컬에서 실행 중인 웹 서비스에 공용 엔드포인트로부터 안전한 터널을 생성하는 리버스 프록시."
content_hash: fdfefd475abadd17aaab8269dc280b6e937bd2bf
last_modified_at: 2024-11-05
related_topics:
  - title: Deutsch version
    url: /de/common/ngrok.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ngrok.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ngrok.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ngrok

로컬에서 실행 중인 웹 서비스에 공용 엔드포인트로부터 안전한 터널을 생성하는 리버스 프록시.
더 많은 정보: <https://ngrok.com>.

- 지정된 포트로 로컬 HTTP 서비스 노출:

`ngrok http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>

- 특정 호스트에서 로컬 HTTP 서비스 노출:

`ngrok http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo.dev</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>

- 로컬 HTTPS 서버 노출:

`ngrok http https://localhost`

- 지정된 포트로 TCP 트래픽 노출:

`ngrok tcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22</span>

- 특정 호스트 및 포트를 위한 TLS 트래픽 노출:

`ngrok tls -hostname=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">443</span>
