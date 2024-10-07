---
layout: page
title: common/git-show-index (한국어)
description: "Git 저장소의 패키지된 아카이브 색인 표시."
content_hash: 26e9ce41b39837e53ae30255962779a9c67ebba6
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-show-index.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-show-index.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git show-index

Git 저장소의 패키지된 아카이브 색인 표시.
더 많은 정보: <https://git-scm.com/docs/git-show-index>.

- Git 패키지 파일의 IDX 파일을 읽고 내용을 `stdout`에 덤프:

`git show-index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.idx</span>

- 색인 파일의 해시 알고리즘 지정 (실험적):

`git show-index --object-format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sha1|sha256</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
