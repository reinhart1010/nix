---
layout: page
title: common/glab-mr-merge (한국어)
description: "GitLab 병합 요청을 관리."
content_hash: ebbba8343b96fbccc2879fd536a41e136b39d9cd
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/glab-mr-merge.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/glab-mr-merge.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># glab mr merge

GitLab 병합 요청을 관리.
더 많은 정보: <https://glab.readthedocs.io/en/latest/mr/merge.html>.

- 현재 브랜치와 관련된 병합 요청을 대화식으로 병합:

`glab mr merge`

- 지정된 병합 요청을 대화식으로 병합:

`glab mr merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mr_번호</span>

- 로컬과 원격 모두에서 브랜치를 제거하여 병합 요청을 병합:

`glab mr merge --remove-source-branch`

- 현재 병합 요청을 메시지 본문과 함께 하나의 커밋으로 스쿼시하고 병합:

`glab mr merge --squash --message="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋_메시지_본체</span>`"`

- 도움말 표시:

`glab mr merge --help`
