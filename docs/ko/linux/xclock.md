---
layout: page
title: linux/xclock (한국어)
description: "아날로그 또는 디지털 형태로 시간을 표시합니다."
content_hash: 590319e1e023060b7d54fa3795d1b0e282d1ecee
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/xclock.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/xclock.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xclock

아날로그 또는 디지털 형태로 시간을 표시합니다.
더 많은 정보: <https://manned.org/xclock>.

- 아날로그 시계 표시:

`xclock`

- 시와 분 필드만 있는 24시간 디지털 시계 표시:

`xclock -digital -brief`

- strftime 형식 문자열을 사용하여 디지털 시계 표시 (strftime(3) 참조):

`xclock -digital -strftime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">형식</span>

- 매 초 업데이트되는 시, 분, 초 필드가 있는 24시간 디지털 시계 표시:

`xclock -digital -strftime '%H:%M:%S' -update 1`

- 시와 분 필드만 있는 12시간 디지털 시계 표시:

`xclock -digital -twelve -brief`
