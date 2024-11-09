---
layout: page
title: linux/ahost (한국어)
description: "호스트 이름 또는 IP 주소와 연결된 A 또는 AAAA 레코드를 표시하는 DNS 조회 도구."
content_hash: f70d5a979a47c8a2848698c68d024337d04527e5
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/ahost.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/ahost.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ahost

호스트 이름 또는 IP 주소와 연결된 A 또는 AAAA 레코드를 표시하는 DNS 조회 도구.
더 많은 정보: <https://manned.org/ahost>.

- 호스트 이름 또는 IP 주소와 연결된 `A` 또는 `AAAA` 레코드 출력:

`ahost `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 추가 디버깅 출력을 표시:

`ahost -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 지정된 유형의 레코드 표시:

`ahost -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a|aaaa|u</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
