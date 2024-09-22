---
layout: page
title: common/bgpgrep (한국어)
description: "MRT 덤프 내의 BGP 데이터 필터링 및 인쇄."
content_hash: 31268f72cd380bbdc58fdd4f427e38eec1493a7e
last_modified_at: 2024-09-22
related_topics:
  - title: Deutsch version
    url: /de/common/bgpgrep.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/bgpgrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bgpgrep

MRT 덤프 내의 BGP 데이터 필터링 및 인쇄.
`gzip`, `bzip2` 및 `xz`로 압축된 파일을 읽을 수 있음.
더 많은 정보: <https://codeberg.org/1414codeforge/ubgpsuite>.

- 모든 경로 나열:

`bgpgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master6.mrt</span>

- 피어의 AS 번호로 결정된 특정 피어로부터 수신된 경로를 나열:

`bgpgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master4.mrt</span>` -peer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">64498</span>

- 피어의 IP 주소로 결정된 특정 피어로부터 수신된 경로를 나열:

`bgpgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master4.mrt.bz2</span>` -peer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2001:db8:dead:cafe:acd::19e</span>

- AS 경로에 특정 ASN이 있는 경로를 나열:

`bgpgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master6.mrt.bz2</span>` -aspath '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">64498 64510</span>`'`

- 특정 주소로 연결되는 경로 목록:

`bgpgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master6.mrt.bz2</span>` -supernet '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2001:db8:dead:cafe:aef::5</span>`'`

- 특정 AS의 커뮤니티가 있는 경로를 나열:

`bgpgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master4.mrt</span>` -communities \( '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">64497</span>`:*' \)`
