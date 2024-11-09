---
layout: page
title: linux/upower (한국어)
description: "전원 및 배터리 정보와 통계를 제공하는 시스템 유틸리티."
content_hash: 9ca27fef2671eaa73c8ca810aff18d84bf86bd71
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/upower.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/upower.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># upower

전원 및 배터리 정보와 통계를 제공하는 시스템 유틸리티.
더 많은 정보: <https://upower.freedesktop.org/docs/upower.1.html>.

- 전원 및 배터리 정보 표시:

`upower --dump`

- 모든 전원 장치 나열:

`upower --enumerate`

- 전원 상태 변화를 감시하고 출력:

`upower --monitor`

- 자세한 전원 상태 변화를 감시하고 출력:

`upower --monitor-detail`

- 버전 표시:

`upower --version`
