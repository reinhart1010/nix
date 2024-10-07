---
layout: page
title: common/git-credential-store (한국어)
description: "디스크에 비밀번호를 저장하는 `git` 도우미."
content_hash: 81c6956202ff9fe8e7974d1405570806b6d5dc8f
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-credential-store.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-credential-store.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git credential-store

디스크에 비밀번호를 저장하는 `git` 도우미.
더 많은 정보: <https://git-scm.com/docs/git-credential-store>.

- 특정 파일에 Git 자격 증명 저장:

`git config credential.helper 'store --file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>`'`
