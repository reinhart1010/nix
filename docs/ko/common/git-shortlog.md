---
layout: page
title: common/git-shortlog (한국어)
description: "`git log` 출력을 요약."
content_hash: a744e50af82d7e4fc280ec54bacac5c4b2570e30
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/git-shortlog.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-shortlog.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-shortlog.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-shortlog.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-shortlog.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git shortlog

`git log` 출력을 요약.
더 많은 정보: <https://git-scm.com/docs/git-shortlog>.

- 작성자 이름별로 알파벳 순으로 그룹화된 모든 커밋 요약 보기:

`git shortlog`

- 커밋 수에 따라 정렬된 모든 커밋 요약 보기:

`git shortlog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--numbered</span>

- 커미터의 신원(이름과 이메일)별로 그룹화된 모든 커밋 요약 보기:

`git shortlog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--committer</span>

- 마지막 5개의 커밋 요약 보기(즉, 리비전 범위 지정):

`git shortlog HEAD~5..HEAD`

- 현재 브랜치에서 모든 사용자, 이메일 및 커밋 수 요약 보기:

`git shortlog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--summary</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--numbered</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-e|--email</span>

- 모든 브랜치에서 모든 사용자, 이메일 및 커밋 수 요약 보기:

`git shortlog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--summary</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--numbered</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-e|--email</span>` --all`
