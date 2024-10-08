---
layout: page
title: common/git-pr (한국어)
description: "GitHub 풀 리퀘스트를 로컬에서 체크아웃."
content_hash: 9214702b4ac76def607c21bb3b497f13e50b1b8f
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-pr.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-pr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-pr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-pr.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-pr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git pr

GitHub 풀 리퀘스트를 로컬에서 체크아웃.
`git-extras`의 일부.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-pr>.

- 특정 풀 리퀘스트를 체크아웃:

`git pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_number</span>

- 특정 원격 저장소에서 풀 리퀘스트를 체크아웃:

`git pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote</span>

- URL에서 풀 리퀘스트를 체크아웃:

`git pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 오래된 풀 리퀘스트 브랜치 정리:

`git pr clean`
