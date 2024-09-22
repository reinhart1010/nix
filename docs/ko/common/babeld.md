---
layout: page
title: common/babeld (한국어)
description: "방화벽-스타일 필터를 사용하는 Babel용 라우팅 데몬입니다."
content_hash: 2e3f7cc13f5df20aaa077a3ec1261413fcd896e8
last_modified_at: 2024-09-22
related_topics:
  - title: Deutsch version
    url: /de/common/babeld.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/babeld.html
    icon: bi bi-globe
tldri18n_status: 2
---
# babeld

방화벽-스타일 필터를 사용하는 Babel용 라우팅 데몬입니다.
더 많은 정보: <https://www.irif.fr/~jch/software/babel/babeld.html>.

- 하나 이상의 구성([c]onfiguration) 파일을 사용하여 데몬을 시작 (순서대로 읽음):

`babeld -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/ports.conf</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/filters.conf</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/interfaces.conf</span>

- 시작 후 데몬화([D]eamonize):

`babeld -D`

- 구성([C]onfiguration) 명령어를 지정:

`babeld -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'redistribute metric 256'</span>

- 작동할 인터페이스를 지정:

`babeld `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>
