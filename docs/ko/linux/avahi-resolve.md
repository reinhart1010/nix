---
layout: page
title: linux/avahi-resolve (한국어)
description: "호스트 이름과 IP 주소 간 변환."
content_hash: ff8bdd08b0c1794359a160bb69ae9fb0876f81ae
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/avahi-resolve.html
    icon: bi bi-globe
tldri18n_status: 2
---
# avahi-resolve

호스트 이름과 IP 주소 간 변환.
더 많은 정보: <https://www.avahi.org/>.

- 로컬 서비스를 IPv4로 변환:

`avahi-resolve -4 --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service.local</span>

- IP를 호스트 이름으로 변환, 자세히:

`avahi-resolve --verbose --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>
