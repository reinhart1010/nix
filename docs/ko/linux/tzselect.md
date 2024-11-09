---
layout: page
title: linux/tzselect (한국어)
description: "대화형으로 시간대를 선택합니다."
content_hash: 9b51319f77ce8b6b6b4fe4a96313b39bcf91b9f6
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/tzselect.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/tzselect.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tzselect

대화형으로 시간대를 선택합니다.
참고: 이 프로그램은 실제로 시간대를 설정하지 않습니다.
더 많은 정보: <https://manned.org/tzselect>.

- 시간대 선택을 위한 대화형 메뉴를 열고 선택한 시간대를 `stdout`에 출력:

`tzselect`

- ISO 6709 표기법으로 좌표에 가장 가까운 시간대 요청:

`tzselect -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">좌표</span>
