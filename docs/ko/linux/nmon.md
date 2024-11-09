---
layout: page
title: linux/nmon (한국어)
description: "시스템 관리자, 튜너 및 벤치마크 도구."
content_hash: 8029d7bd612262a3ecd06c5d472e3833418ecf04
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/nmon.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/nmon.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nmon

시스템 관리자, 튜너 및 벤치마크 도구.
더 많은 정보: <https://manned.org/nmon>.

- `nmon` 시작:

`nmon`

- 기록을 파일에 저장 ("-s 300 -c 288" 기본값):

`nmon -f`

- 각 측정 사이에 30초를 두고 총 240번의 측정을 기록하여 파일에 저장:

`nmon -f -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">240</span>
