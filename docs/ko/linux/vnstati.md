---
layout: page
title: linux/vnstati (한국어)
description: "vnStat의 PNG 이미지 출력 지원."
content_hash: 0d06a55a92bcdf2076c4efa54d7757068ed7ef86
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/vnstati.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/vnstati.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vnstati

vnStat의 PNG 이미지 출력 지원.
더 많은 정보: <https://manned.org/vnstati>.

- 지난 2개월, 일별 및 전체 요약 출력:

`vnstati --summary --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네트워크_인터페이스</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.png</span>

- 역대 트래픽이 가장 많은 10일 출력:

`vnstati --top 10 --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네트워크_인터페이스</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.png</span>

- 지난 12개월의 월별 트래픽 통계 출력:

`vnstati --months --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네트워크_인터페이스</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.png</span>

- 지난 24시간의 시간별 트래픽 통계 출력:

`vnstati --hours --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네트워크_인터페이스</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.png</span>
