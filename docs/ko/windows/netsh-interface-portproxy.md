---
layout: page
title: windows/netsh-interface-portproxy (한국어)
description: "다양한 네트워크 구성 요소의 상태를 구성하고 표시합니다."
content_hash: 0562e97232feabbc5060b9b52b64e523dde09667
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/windows/netsh-interface-portproxy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# netsh interface portproxy

다양한 네트워크 구성 요소의 상태를 구성하고 표시합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/networking/technologies/netsh/netsh-interface-portproxy>.

- 현재 포트 전달 설정 표시:

`netsh interface portproxy show all`

- IPv4 포트 전달 설정 (관리자 권한 콘솔에서 실행):

`netsh interface portproxy add v4tov4 listenaddress=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1</span>` listenport=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>`  connectaddress=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.1</span>` connectport=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>

- IPv4 포트 전달 삭제 (관리자 권한 콘솔에서 실행):

`netsh interface portproxy delete v4tov4 listenaddress=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1</span>` listenport=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>

- 도움말 표시:

`netsh interface portproxy`
