---
layout: page
title: common/git-svn (한국어)
description: "Subversion 저장소와 Git 간의 양방향 작업."
content_hash: 2240b016396f3bb007b19f7b384dca489784a25d
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-svn.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-svn.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-svn.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-svn.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-svn.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-svn.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git svn

Subversion 저장소와 Git 간의 양방향 작업.
더 많은 정보: <https://git-scm.com/docs/git-svn>.

- SVN 저장소 클론:

`git svn clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/subversion_repo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_dir</span>

- 특정 리비전 번호에서 시작하여 SVN 저장소 클론:

`git svn clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--revision</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>`:HEAD `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://svn.example.net/subversion/repo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_dir</span>

- 원격 SVN 저장소에서 로컬 클론 업데이트:

`git svn rebase`

- Git HEAD를 변경하지 않고 원격 SVN 저장소에서 업데이트 가져오기:

`git svn fetch`

- SVN 저장소에 커밋:

`git svn commit`
