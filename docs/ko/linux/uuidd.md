---
layout: page
title: linux/uuidd (한국어)
description: "UUID 생성을 위한 데몬."
content_hash: ffb561e37284f747817dc795abed959110157715
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/uuidd.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/uuidd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/uuidd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># uuidd

UUID 생성을 위한 데몬.
더 많은 정보: <https://manned.org/uuidd>.

- 무작위 UUID 생성:

`uuidd --random`

- 다수의 무작위 UUID 생성:

`uuidd --random --uuids `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UUID_개수</span>

- 현재 시간과 시스템의 MAC 주소를 기반으로 한 시간 기반 UUID 생성:

`uuidd --time`
