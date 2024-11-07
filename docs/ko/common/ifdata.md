---
layout: page
title: common/ifdata (한국어)
description: "네트워크 인터페이스에 대한 정보를 표시."
content_hash: bd004486997c3e0c2c26212c069b572cc8cc5cbb
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/ifdata.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ifdata

네트워크 인터페이스에 대한 정보를 표시.
더 많은 정보: <https://joeyh.name/code/moreutils/>.

- 지정된 인터페이스의 전체 구성을 표시:

`ifdata -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 종료 코드를 통해 지정된 인터페이스의 존재([e]xistence)를 나타냄:

`ifdata -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 지정된 인터페이스의 IPv4 주소([a]ddress)와 넷마스크([n]etmask)를 표시:

`ifdata -pa -pn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 네트워크([N]etwork) 주소, 브로드캐스트([b]roadcast) 주소 및 지정된 인터페이스의 MTU를 표시:

`ifdata -pN -pb -pm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 도움말 표시:

`ifdata`
