---
layout: page
title: linux/cgcreate (한국어)
description: "cgroup을 생성하여 프로세스가 사용하는 자원을 제한, 측정 및 제어."
content_hash: 000353e845c0f8ac8e8f0affc520802e3619b94c
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/cgcreate.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/cgcreate.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/cgcreate.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/cgcreate.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cgcreate

cgroup을 생성하여 프로세스가 사용하는 자원을 제한, 측정 및 제어.
`cgroups`의 유형은 `memory`, `cpu`, `net_cls` 등이 있습니다.
더 많은 정보: <https://manned.org/cgcreate>.

- 새 그룹 생성:

`cgcreate -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_유형</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_이름</span>

- 여러 cgroup 유형으로 새 그룹 생성:

`cgcreate -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_유형1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_유형2</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_이름</span>

- 하위 그룹 생성:

`mkdir /sys/fs/cgroup/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_유형</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_이름</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위_그룹_이름</span>
