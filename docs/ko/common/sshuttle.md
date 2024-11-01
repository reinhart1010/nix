---
layout: page
title: common/sshuttle (한국어)
description: "SSH 연결을 통해 트래픽을 터널링하는 투명 프록시 서버."
content_hash: 733d18f0d7b986c8e4861630076db890c7ab07c7
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/sshuttle.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/sshuttle.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sshuttle.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sshuttle

SSH 연결을 통해 트래픽을 터널링하는 투명 프록시 서버.
원격 SSH 서버에서는 루트 권한이나 특별한 설정이 필요하지 않지만, 로컬 머신에서는 루트 접근이 요청됩니다.
더 많은 정보: <https://manned.org/sshuttle>.

- 원격 SSH 서버를 통해 모든 IPv4 TCP 트래픽 전달:

`sshuttle --remote=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh서버</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.0.0.0/0</span>

- 서버의 기본 DNS 해석기로 모든 DNS 트래픽도 전달:

`sshuttle --dns --remote=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh서버</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.0.0.0/0</span>

- 특정 서브넷으로 향하는 트래픽을 제외한 모든 트래픽 전달:

`sshuttle --remote=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh서버</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.0.0.0/0</span>` --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1/24</span>

- tproxy 방법을 사용하여 모든 IPv4 및 IPv6 트래픽 전달:

`sshuttle --method=tproxy --remote=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh서버</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.0.0.0/0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">::/0</span>` --exclude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">내_로컬_ip_주소</span>` --exclude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh_서버_ip_주소</span>
