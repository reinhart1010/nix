---
layout: page
title: linux/numactl (한국어)
description: "프로세스 또는 공유 메모리에 대한 NUMA 정책 제어."
content_hash: 60bcdfe047512874ddea1c0ff7057f805ebdcb7e
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/numactl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/numactl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># numactl

프로세스 또는 공유 메모리에 대한 NUMA 정책 제어.
더 많은 정보: <https://manned.org/numactl>.

- 노드 0에서 명령을 실행하고 메모리는 노드 0과 1에 할당:

`numactl --cpunodebind=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` --membind=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0,1</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령_인자들</span>

- 현재 CPU 세트의 CPU(코어) 0-4 및 8-12에서 명령 실행:

`numactl --physcpubind=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+0-4,8-12</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령_인자들</span>

- 모든 CPU에 메모리를 인터리브하여 명령 실행:

`numactl --interleave=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령_인자들</span>
