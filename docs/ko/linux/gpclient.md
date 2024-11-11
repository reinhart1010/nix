---
layout: page
title: linux/gpclient (한국어)
description: "OpenConnect를 통해 Linux에서 GlobalProtect VPN에 연결."
content_hash: 31ce4cab53e8d1f41a3b3ae416d748cd18ba8b4b
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/gpclient.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/gpclient.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gpclient

OpenConnect를 통해 Linux에서 GlobalProtect VPN에 연결.
더 많은 정보: <https://github.com/yuezk/GlobalProtect-openconnect>.

- 포털 서버를 사용하여 GlobalProtect VPN에 연결:

`gpclient connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vpn_게이트웨이_URL</span>

- 현재 연결된 VPN 서버에서 연결 해제:

`gpclient disconnect`

- VPN 관리를 위한 그래픽 사용자 인터페이스(GUI) 실행:

`gpclient launch-gui`

- OpenSSL 우회 방법을 사용하여 레거시 재협상 오류 우회:

`gpclient connect --fix-openssl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vpn_게이트웨이_URL</span>

- 연결 중 TLS 오류 무시:

`gpclient connect --ignore-tls-errors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vpn_게이트웨이_URL</span>

- 버전 표시:

`gpclient --version`

- 명령에 대한 도움말 표시:

`gpclient help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>
