---
layout: page
title: common/git-repack (한국어)
description: "Git 저장소에서 압축되지 않은 객체를 패킹."
content_hash: e9e41ba0f54adc9e170716f357e62dfbf7b65322
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-repack.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-repack.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-repack.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-repack.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-repack.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git repack

Git 저장소에서 압축되지 않은 객체를 패킹.
더 많은 정보: <https://git-scm.com/docs/git-repack>.

- 현재 디렉토리에서 압축되지 않은 객체를 패킹:

`git repack`

- 패킹 후 중복 객체도 제거:

`git repack -d`
