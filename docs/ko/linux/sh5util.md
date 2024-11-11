---
layout: page
title: linux/sh5util (한국어)
description: "`sacct_gather_profile` 플러그인이 생성한 HDF5 파일 병합 도구."
content_hash: 5d8107ce3e225330179de7ccbfd2596a50740b21
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/sh5util.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/sh5util.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sh5util

`sacct_gather_profile` 플러그인이 생성한 HDF5 파일 병합 도구.
더 많은 정보: <https://slurm.schedmd.com/sh5util.html>.

- 지정된 작업 또는 단계에 대해 각 할당된 노드에서 생성된 HDF5 파일 병합:

`sh5util --jobs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID|작업_ID.단계_ID</span>

- 병합된 작업 파일에서 하나 이상의 데이터 시리즈 추출:

`sh5util --jobs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID|작업_ID.단계_ID</span>` --extract -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.h5</span>` --series=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Energy|Filesystem|Network|Task</span>

- 병합된 작업 파일에서 모든 노드의 하나의 데이터 항목 추출:

`sh5util --jobs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID|작업_ID.단계_ID</span>` --item-extract --series=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Energy|Filesystem|Network|Task</span>` --data=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터_항목</span>
