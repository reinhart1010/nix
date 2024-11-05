---
layout: page
title: common/nping (한국어)
description: "네트워크 패킷 생성 도구/핑 유틸리티."
content_hash: 1799d1b980eb83b5e784858549b4ad68101500b5
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/nping.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nping.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nping

네트워크 패킷 생성 도구/핑 유틸리티.
더 많은 정보: <https://nmap.org/nping/>.

- 사용자가 허용된 경우 ICMP를 사용하여 지정된 호스트에 핑, 그렇지 않으면 TCP 사용:

`nping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 사용자가 허용된 경우 ICMP를 사용하여 지정된 호스트에 핑:

`nping --icmp --privileged `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- UDP를 사용하여 지정된 호스트에 핑:

`nping --udp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 지정된 포트에서 TCP를 사용하여 지정된 호스트에 핑:

`nping --tcp --dest-port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">443</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 특정 횟수만큼 핑:

`nping --count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 각 핑 사이에 일정 시간 대기:

`nping --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5s</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 지정된 인터페이스를 통해 요청 전송:

`nping --interface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- IP 범위에 핑:

`nping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.1-10</span>
