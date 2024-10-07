---
layout: page
title: common/git-check-ref-format (한국어)
description: "참조 이름이 적절한지 확인하고, 그렇지 않으면 0이 아닌 상태로 종료."
content_hash: 3a3095b1e1c1fa2454afbbffc0a5f507580201e3
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-check-ref-format.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-check-ref-format.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-check-ref-format.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-check-ref-format.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git check-ref-format

참조 이름이 적절한지 확인하고, 그렇지 않으면 0이 아닌 상태로 종료.
더 많은 정보: <https://git-scm.com/docs/git-check-ref-format>.

- 지정된 참조 이름의 형식 확인:

`git check-ref-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">refs/head/refname</span>

- 마지막으로 체크아웃한 브랜치 이름 출력:

`git check-ref-format --branch @{-1}`

- 참조 이름을 정규화:

`git check-ref-format --normalize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">refs/head/refname</span>
