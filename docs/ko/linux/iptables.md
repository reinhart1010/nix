---
layout: page
title: linux/iptables (한국어)
description: "Linux 커널 IPv4 방화벽의 테이블, 체인 및 규칙을 구성합니다."
content_hash: 7f13bb144c37c8a428ee8d508c7eff5b746a0d84
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/iptables.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/iptables.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/iptables.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/iptables.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/iptables.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># iptables

Linux 커널 IPv4 방화벽의 테이블, 체인 및 규칙을 구성합니다.
IPv6 트래픽 규칙 설정을 위해서는 `ip6tables`를 사용하세요. 같이 보기: `iptables-save`, `iptables-restore`.
더 많은 정보: <https://manned.org/iptables>.

- 필터 테이블의 체인, 규칙, 패킷/바이트 카운터 및 라인 번호 보기:

`sudo iptables --verbose --numeric --list --line-numbers`

- 체인 [P]규칙 설정:

`sudo iptables --policy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">체인</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">규칙</span>

- IP에 대한 체인 정책에 규칙 [A]추가:

`sudo iptables --append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">체인</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>` --jump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">규칙</span>

- [p]프로토콜과 포트를 고려하여 IP에 대한 체인 정책에 규칙 [A]추가:

`sudo iptables --append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">체인</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>` --protocol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp|udp|icmp|...</span>` --dport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` --jump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">규칙</span>

- `192.168.0.0/24` 서브넷의 모든 트래픽을 호스트의 공인 IP로 변환하는 NAT 규칙 추가:

`sudo iptables --table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nat</span>` --append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">POSTROUTING</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.0/24</span>` --jump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MASQUERADE</span>

- 체인 규칙 [D]삭제:

`sudo iptables --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">체인</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">규칙_라인_번호</span>
