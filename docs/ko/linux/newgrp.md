---
layout: page
title: linux/newgrp (한국어)
description: "기본 그룹 소속을 변경합니다."
content_hash: 5009f7cc543f3ba46184c21b4a07988f83c12e96
last_modified_at: 2024-11-09
related_topics:
  - title: català version
    url: /ca/linux/newgrp.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/newgrp.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/newgrp.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/newgrp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/newgrp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># newgrp

기본 그룹 소속을 변경합니다.
더 많은 정보: <https://manned.org/newgrp>.

- 사용자의 기본 그룹 소속을 변경:

`newgrp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_이름</span>

- `/etc/passwd`에 설정된 사용자의 기본 그룹으로 리셋:

`newgrp`
