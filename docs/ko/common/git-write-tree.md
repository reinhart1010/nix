---
layout: page
title: common/git-write-tree (한국어)
description: "현재 색인에서 트리 객체를 생성하는 저수준 유틸리티."
content_hash: 9c14f013d61dd58a3fe483ef71d8c1b495dbb7de
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-write-tree.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-write-tree.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git write-tree

현재 색인에서 트리 객체를 생성하는 저수준 유틸리티.
더 많은 정보: <https://git-scm.com/docs/git-write-tree>.

- 현재 색인에서 트리 객체 생성:

`git write-tree`

- 디렉토리가 참조하는 객체가 객체 데이터베이스에 존재하는지 확인하지 않고 트리 객체 생성:

`git write-tree --missing-ok`

- 하위 디렉토리를 나타내는 트리 객체 생성 (지정된 하위 디렉토리에 대한 하위 프로젝트의 트리 객체를 작성할 때 사용):

`git write-tree --prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위_디렉토리</span>`/`
