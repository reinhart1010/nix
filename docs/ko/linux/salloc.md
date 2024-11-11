---
layout: page
title: linux/salloc (한국어)
description: "클러스터에서 하나 이상의 노드를 할당하여 대화형 셸 세션을 시작하거나 명령을 실행합니다."
content_hash: 017b3929ab2f188384c0eee68552255e9b51f369
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/salloc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/salloc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># salloc

클러스터에서 하나 이상의 노드를 할당하여 대화형 셸 세션을 시작하거나 명령을 실행합니다.
더 많은 정보: <https://slurm.schedmd.com/salloc.html>.

- 클러스터의 노드에서 대화형 셸 세션 시작:

`salloc`

- 클러스터의 노드에서 지정된 명령을 동기적으로 실행:

`salloc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -a</span>

- 지정된 제약 조건을 충족하는 노드만 할당:

`salloc --constraint=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(amd|intel)&gpu</span>
