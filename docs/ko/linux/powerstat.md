---
layout: page
title: linux/powerstat (한국어)
description: "배터리 전원 소스를 사용하거나 RAPL 인터페이스를 지원하는 컴퓨터의 전력 소비를 측정합니다."
content_hash: ce184ecd4329adeefec2d141c8eeed418723e4ee
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/powerstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# powerstat

배터리 전원 소스를 사용하거나 RAPL 인터페이스를 지원하는 컴퓨터의 전력 소비를 측정합니다.
더 많은 정보: <https://manned.org/powerstat>.

- 10초 간격으로 10번 샘플링하여 전력 측정:

`powerstat`

- 사용자 지정 간격과 샘플 수로 전력 측정:

`powerstat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">간격</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">샘플_수</span>

- Intel의 RAPL 인터페이스를 사용하여 전력 측정:

`powerstat -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">간격</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">샘플_수</span>

- 전력 측정의 히스토그램 표시:

`powerstat -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">간격</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">샘플_수</span>

- 모든 통계 수집 옵션 활성화:

`powerstat -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">간격</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">샘플_수</span>
