---
layout: page
title: common/git-credential-cache (한국어)
description: "Git 비밀번호를 메모리에 임시로 저장하는 도구."
content_hash: b72352938aae09269ae7b994c4b8e9b1c06e32b0
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-credential-cache.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-credential-cache.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git credential-cache

Git 비밀번호를 메모리에 임시로 저장하는 도구.
더 많은 정보: <https://git-scm.com/docs/git-credential-cache>.

- Git 자격 증명을 특정 시간 동안 저장:

`git config credential.helper 'cache --timeout=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">초단위_시간</span>`'`
