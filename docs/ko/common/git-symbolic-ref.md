---
layout: page
title: common/git-symbolic-ref (한국어)
description: "참조를 저장하는 파일을 읽고, 변경하거나 삭제합니다."
content_hash: 5e60793cbdf4fc5ae68ee930c3458762c477213b
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-symbolic-ref.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-symbolic-ref.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git symbolic-ref

참조를 저장하는 파일을 읽고, 변경하거나 삭제합니다.
더 많은 정보: <https://git-scm.com/docs/git-symbolic-ref>.

- 이름으로 참조 저장:

`git symbolic-ref refs/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">참조</span>

- 업데이트 이유를 포함한 메시지와 함께 이름으로 참조 저장:

`git symbolic-ref -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`" refs/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` refs/heads/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>

- 이름으로 참조 읽기:

`git symbolic-ref refs/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 이름으로 참조 삭제:

`git symbolic-ref --delete refs/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 스크립팅을 위해 `--quiet`로 오류를 숨기고 `--short`를 사용하여 간소화하기 ("refs/heads/X"가 "X"로 출력됨):

`git symbolic-ref --quiet --short refs/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>
