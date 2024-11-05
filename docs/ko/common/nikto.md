---
layout: page
title: common/nikto (한국어)
description: "웹 서버에 대해 여러 항목에 대한 테스트를 수행하는 웹 서버 스캐너."
content_hash: e39a30fc17ff9dab8b3c4b6f80ee38d839c8b984
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/nikto.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nikto.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nikto

웹 서버에 대해 여러 항목에 대한 테스트를 수행하는 웹 서버 스캐너.
더 많은 정보: <https://cirt.net/Nikto2>.

- 대상 호스트에 대해 기본 Nikto 스캔 수행:

`perl nikto.pl -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1</span>

- 기본 스캔을 수행할 때 포트 번호 지정:

`perl nikto.pl -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">443</span>

- 전체 URL 구문을 사용하여 포트 및 프로토콜 스캔:

`perl nikto.pl -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://192.168.0.1:443/</span>

- 동일한 스캔 세션에서 여러 포트 스캔:

`perl nikto.pl -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80,88,443</span>

- 최신 플러그인 및 데이터베이스로 업데이트:

`perl nikto.pl -update`
