---
layout: page
title: linux/firewall-cmd (한국어)
description: "firewalld 명령줄 클라이언트."
content_hash: be3cc7f18cf3c1c8bfe10df41d65736c3fa09058
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/firewall-cmd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/firewall-cmd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># firewall-cmd

firewalld 명령줄 클라이언트.
런타임 또는 영구 방화벽 구성 상태를 조회 및 수정.
더 많은 정보: <https://firewalld.org/documentation/man-pages/firewall-cmd>.

- 런타임 구성 상태에서 사용 가능한 모든 방화벽 영역과 규칙 조회:

`firewall-cmd --list-all-zones`

- 인터페이스를 block 영역으로 영구적으로 이동하여 모든 통신 차단:

`firewall-cmd --permanent --zone=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">block</span>` --change-interface=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enp1s0</span>

- 지정된 영역에서 서비스의 포트를 영구적으로 열기 (예: `public` 영역에서 포트 443):

`firewall-cmd --permanent --zone=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">public</span>` --add-service=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https</span>

- 지정된 영역에서 서비스의 포트를 영구적으로 닫기 (예: `public` 영역에서 포트 80):

`firewall-cmd --permanent --zone=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">public</span>` --remove-service=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http</span>

- 지정된 영역에서 들어오는 패킷의 포트를 영구적으로 포워딩 (예: `public` 영역에서 포트 443을 8443으로):

`firewall-cmd --permanent --zone=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">public</span>` --add-rich-rule='rule family="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ipv4|ipv6</span>`" forward-port port="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">443</span>`" protocol="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">udp|tcp</span>`" to-port="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8443</span>`"'`

- firewalld를 다시 로드하여 런타임 변경 사항을 제거하고 영구 구성을 즉시 적용:

`firewall-cmd --reload`

- 런타임 구성 상태를 영구 구성으로 저장:

`firewall-cmd --runtime-to-permanent`

- 비상시 패닉 모드 활성화. 모든 트래픽이 차단되고 활성 연결이 종료됨:

`firewall-cmd --panic-on`
