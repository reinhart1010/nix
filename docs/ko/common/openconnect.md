---
layout: page
title: common/openconnect (한국어)
description: "Cisco AnyConnect VPN 및 기타 VPN을 위한 VPN 클라이언트."
content_hash: 0fde08cd41942d33f0d95fef0941b2137a532cba
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/openconnect.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/openconnect.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># openconnect

Cisco AnyConnect VPN 및 기타 VPN을 위한 VPN 클라이언트.
더 많은 정보: <https://www.infradead.org/openconnect/manual.html>.

- 서버에 연결:

`openconnect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vpn.example.org</span>

- 백그라운드에서 실행되도록 서버에 연결:

`openconnect --background `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vpn.example.org</span>

- 백그라운드에서 실행 중인 연결 종료:

`killall -SIGINT openconnect`

- 설정 파일에서 옵션을 읽어 서버에 연결:

`openconnect --config=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vpn.example.org</span>

- 특정 SSL 클라이언트 인증서로 인증하여 서버에 연결:

`openconnect --certificate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vpn.example.org</span>
