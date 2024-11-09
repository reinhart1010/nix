---
layout: page
title: linux/kpartx (한국어)
description: "파티션 테이블에서 디바이스 맵 생성."
content_hash: d38c19551ca07499765ad763e23c63d286e3adc9
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/kpartx.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/kpartx.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kpartx

파티션 테이블에서 디바이스 맵 생성.
더 많은 정보: <https://manned.org/kpartx>.

- 파티션 매핑 추가:

`kpartx -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디스크_전체.img</span>

- 파티션 매핑 삭제:

`kpartx -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디스크_전체.img</span>

- 파티션 매핑 나열:

`kpartx -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디스크_전체.img</span>
