---
layout: page
title: common/sc_wartsfilter (한국어)
description: "`warts` 파일에서 특정 레코드를 선택."
content_hash: a5c23451b3f28fb981fd0bd8b2341b9f17012f43
last_modified_at: 2024-11-10
related_topics:
  - title: Deutsch version
    url: /de/common/sc_wartsfilter.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/sc_wartsfilter.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sc_wartsfilter

`warts` 파일에서 특정 레코드를 선택.
더 많은 정보: <https://www.caida.org/catalog/software/scamper/>.

- 특정 목적지를 가진 모든 데이터 레코드를 필터링하여 별도의 파일로 저장:

`sc_wartsfilter -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.warts</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.warts</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.0.2.5</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.0.2.6</span>

- 특정 접두사를 가진 목적지의 모든 레코드를 필터링하여 별도의 파일로 저장:

`sc_wartsfilter -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.warts</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.warts</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2001:db8::/32</span>

- 특정 작업을 사용한 모든 레코드를 필터링하여 JSON으로 출력:

`sc_wartsfilter -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.warts</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ping</span>` | sc_warts2json`
