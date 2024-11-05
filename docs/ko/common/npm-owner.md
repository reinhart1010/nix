---
layout: page
title: common/npm-owner (한국어)
description: "게시된 패키지의 소유권 관리."
content_hash: f4990bb6b076ecb8b9276b4ae07f9bb58c6b7e61
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/npm-owner.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/npm-owner.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># npm-owner

게시된 패키지의 소유권 관리.
더 많은 정보: <https://docs.npmjs.com/cli/commands/npm-owner>.

- 새 사용자를 패키지의 관리자로 추가:

`npm owner add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>

- 사용자를 패키지의 소유자 목록에서 제거:

`npm owner rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>

- 패키지의 모든 소유자 나열:

`npm owner ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>
