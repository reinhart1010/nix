---
layout: page
title: common/naabu (한국어)
description: "신뢰성과 단순성에 중점을 둔 Go로 작성된 빠른 포트 스캐너."
content_hash: df0cc6cce7d7ef06851001fd1bb14b3d868db7f5
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/naabu.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/naabu.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/naabu.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># naabu

신뢰성과 단순성에 중점을 둔 Go로 작성된 빠른 포트 스캐너.
참고: 일부 기능은 `naabu`를 루트 권한으로 실행할 때만 활성화되며, 예를 들어 SYN 스캔이 있습니다.
더 많은 정보: <https://github.com/projectdiscovery/naabu>.

- 원격 호스트의 기본(상위 100개) 포트에 대해 SYN 스캔 실행:

`sudo naabu -host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 사용 가능한 네트워크 인터페이스와 로컬 호스트의 공용 IP 주소 표시:

`naabu -interface-list`

- 원격 호스트의 모든 포트 스캔 (CONNECT 스캔, `sudo` 없이):

`naabu -p - -host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 원격 호스트의 상위 1000개 포트 스캔:

`naabu -top-ports 1000 -host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 원격 호스트의 TCP 포트 80, 443 및 UDP 포트 53 스캔:

`naabu -p 80,443,u:53 -host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 원격 호스트가 사용하는 CDN 유형 표시 (있는 경우):

`naabu -p 80,443 -cdn -host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 추가 기능을 위해 `naabu`에서 `nmap` 실행 (`nmap`이 설치되어 있어야 함):

`sudo naabu -v -host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` -nmap-cli 'nmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v -T5 -sC</span>`'`
