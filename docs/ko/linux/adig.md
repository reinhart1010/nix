---
layout: page
title: linux/adig (한국어)
description: "도메인 네임 시스템(DNS) 서버에서 받은 정보를 출력합니다."
content_hash: 9a8d86d7cb2a656cbca5477d605676fbe8a261bf
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/adig.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/adig.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/adig.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/adig.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># adig

도메인 네임 시스템(DNS) 서버에서 받은 정보를 출력합니다.
더 많은 정보: <https://manned.org/adig>.

- 호스트 이름에 대한 A (기본) 레코드를 DNS에서 표시:

`adig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 추가 [d]디버깅 출력 표시:

`adig -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 특정 DNS [s]서버에 연결:

`adig -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3.4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- DNS 서버에 연결할 때 특정 TCP 포트 사용:

`adig -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- DNS 서버에 연결할 때 특정 UDP 포트 사용:

`adig -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
