---
layout: page
title: linux/openfortivpn (한국어)
description: "Fortinet의 독점 PPP+SSL VPN 솔루션을 위한 VPN 클라이언트."
content_hash: 4c425c6c3806a159f3a9d9059af49406343c50f5
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/openfortivpn.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/openfortivpn.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># openfortivpn

Fortinet의 독점 PPP+SSL VPN 솔루션을 위한 VPN 클라이언트.
더 많은 정보: <https://github.com/adrienverge/openfortivpn>.

- 사용자명과 비밀번호로 VPN에 연결:

`openfortivpn --username=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` --password=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- 특정 구성 파일을 사용하여 VPN에 연결 (`/etc/openfortivpn/config`가 기본값):

`sudo openfortivpn --config=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성</span>

- 호스트와 포트를 지정하여 VPN에 연결:

`openfortivpn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 인증서의 sha256 합계를 전달하여 특정 게이트웨이를 신뢰:

`openfortivpn --trusted-cert=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sha256_합계</span>
