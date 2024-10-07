---
layout: page
title: common/git-mr (한국어)
description: "GitLab 병합 요청을 로컬에서 체크아웃."
content_hash: 732d3aa2264a145290aeb98bea3617500039aed6
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-mr.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-mr.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git mr

GitLab 병합 요청을 로컬에서 체크아웃.
`git-extras`의 일부.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-mr>.

- 특정 병합 요청 체크아웃:

`git mr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mr_number</span>

- 특정 원격에서 병합 요청 체크아웃:

`git mr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mr_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote</span>

- 병합 요청 URL에서 체크아웃:

`git mr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 오래된 병합 요청 브랜치 정리:

`git mr clean`
