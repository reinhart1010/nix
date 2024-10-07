---
layout: page
title: common/git-cat-file (한국어)
description: "Git 저장소 객체의 콘텐츠 또는 유형 및 크기 정보를 제공합니다."
content_hash: 10a277086452bdcb87f5c40ceef0167ef3dc827f
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-cat-file.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-cat-file.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-cat-file.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-cat-file.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-cat-file.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-cat-file.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-cat-file.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git cat-file

Git 저장소 객체의 콘텐츠 또는 유형 및 크기 정보를 제공합니다.
더 많은 정보: <https://git-scm.com/docs/git-cat-file>.

- HEAD 커밋의 크기(바이트 단위) 확인:

`git cat-file -s HEAD`

- 주어진 Git 객체의 유형(blob, tree, commit, tag) 확인:

`git cat-file -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8c442dc3</span>

- 주어진 Git 객체의 유형에 따라 콘텐츠를 보기 좋게 출력:

`git cat-file -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD~2</span>
