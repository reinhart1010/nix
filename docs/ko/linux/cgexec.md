---
layout: page
title: linux/cgexec (한국어)
description: "프로세스가 사용하는 자원을 제한, 측정 및 제어."
content_hash: b1140a4fa0a486a6f31b11447fcdd33aa8b477ef
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/cgexec.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/cgexec.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/cgexec.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/cgexec.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cgexec

프로세스가 사용하는 자원을 제한, 측정 및 제어.
`cpu`, `memory` 등 여러 cgroup 유형(컨트롤러)이 존재합니다.
더 많은 정보: <https://manned.org/cgexec>.

- 지정된 컨트롤러와 cgroup에서 프로세스를 실행:

`cgexec -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨트롤러</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cgroup_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>
