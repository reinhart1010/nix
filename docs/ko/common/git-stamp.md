---
layout: page
title: common/git-stamp (한국어)
description: "마지막 커밋 메시지에 버그 추적기의 이슈 번호를 참조하거나 리뷰 페이지 링크를 추가합니다."
content_hash: eb8215dbd6ab2a2289ceaaa4aa89b65a4982b420
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-stamp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-stamp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git stamp

마지막 커밋 메시지에 버그 추적기의 이슈 번호를 참조하거나 리뷰 페이지 링크를 추가합니다.
`git-extras`의 일부입니다.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-stamp>.

- 버그 추적기의 이슈 번호를 참조하여 마지막 커밋 메시지에 스탬프 추가:

`git stamp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이슈_번호</span>

- 리뷰 페이지 링크를 추가하여 마지막 커밋 메시지에 스탬프 추가:

`git stamp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리뷰 https://example.org/path/to/review</span>

- 이전 이슈를 새 이슈로 교체하여 마지막 커밋 메시지에 스탬프 추가:

`git stamp --replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이슈_번호</span>
