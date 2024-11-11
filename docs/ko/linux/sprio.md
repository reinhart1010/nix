---
layout: page
title: linux/sprio (한국어)
description: "작업의 스케줄링 우선순위를 결정하는 요소 보기."
content_hash: d838b21846641a7d86557c5dd4ebe83ed4c72f1b
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/sprio.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/sprio.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sprio

작업의 스케줄링 우선순위를 결정하는 요소 보기.
더 많은 정보: <https://slurm.schedmd.com/sprio.html>.

- 모든 작업의 스케줄링 우선순위를 결정하는 요소 보기:

`sprio`

- 지정한 작업의 스케줄링 우선순위를 결정하는 요소 보기:

`sprio --jobs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID_1,작업_ID_2,...</span>

- 추가 정보를 출력:

`sprio --long`

- 지정한 사용자의 작업 정보를 보기:

`sprio --user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_이름_1,사용자_이름_2,...</span>

- 작업 스케줄링 우선순위를 결정하는 각 요소의 가중치 출력:

`sprio --weights`
