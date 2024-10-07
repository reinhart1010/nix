---
layout: page
title: common/git-verify-commit (한국어)
description: "커밋의 GPG 검증 확인."
content_hash: 4a74ed0b09a7d2cc91c584e2d0dd2cb32d35b6be
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-verify-commit.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-verify-commit.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git verify-commit

커밋의 GPG 검증 확인.
커밋이 검증되지 않으면, 지정된 옵션에 상관없이 아무것도 출력되지 않습니다.
더 많은 정보: <https://git-scm.com/docs/git-verify-commit>.

- 커밋에 대한 GPG 서명 확인:

`git verify-commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋_해시1 선택_커밋_해시2 ...</span>

- 커밋에 대한 GPG 서명을 확인하고 각 커밋의 세부 정보를 표시:

`git verify-commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋_해시1 선택_커밋_해시2 ...</span>` --verbose`

- 커밋에 대한 GPG 서명을 확인하고 원시 세부 정보를 출력:

`git verify-commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋_해시1 선택_커밋_해시2 ...</span>` --raw`
