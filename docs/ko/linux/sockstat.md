---
layout: page
title: linux/sockstat (한국어)
description: "열린 인터넷 또는 UNIX 도메인 소켓 나열."
content_hash: 5345d3f80781f805555d3084b959c92b443a8abd
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/sockstat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/sockstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sockstat

열린 인터넷 또는 UNIX 도메인 소켓 나열.
같이 보기: `netstat`.
더 많은 정보: <https://manned.org/sockstat>.

- 대기 중이거나 연결된 IPv4 및 IPv6 소켓 정보 표시:

`sockstat`

- 특정 프로토콜을 사용하여 특정 포트에서 [l]대기 중인 IPv[4]/IPv[6] 소켓 정보 표시:

`sockstat -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4|6</span>` -l -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp|udp|raw|unix</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트1,포트2...</span>

- [c]연결된 소켓 및 [u]유닉스 소켓도 표시:

`sockstat -cu`

- 지정된 `pid` 또는 프로세스의 소켓만 표시:

`sockstat -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid|프로세스</span>

- 지정된 `uid` 또는 사용자의 소켓만 표시:

`sockstat -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|사용자</span>

- 지정된 `gid` 또는 그룹의 소켓만 표시:

`sockstat -G `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gid|그룹</span>
