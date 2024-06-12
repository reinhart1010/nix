---
layout: page
title: common/git-log (한국어)
description: "커밋 이력을 보여줍니다."
content_hash: 525290510abfea3fd3b6280ef583bafae8246218
last_modified_at: 2024-06-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-log.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-log.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-log.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-log.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-log.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-log.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-log.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-log.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-log.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git log

커밋 이력을 보여줍니다.
더 많은 정보: <https://git-scm.com/docs/git-log>.

- 현재 작업 디렉토리의 Git 리포지토리에서 현재 커밋을 기준으로 역순으로 커밋 시퀀스 보기:

`git log`

- 변경 사항을 포함해, 특정 파일 또는 디렉토리의 이력 보기:

`git log -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_또는_디렉토리_경로</span>

- 각 커밋에서 어떤 파일이 변경되었는지 개요 보기:

`git log --stat`

- 현재 브랜치의 커밋 그래프를 첫 줄만 사용해 보기:

`git log --oneline --graph`

- 전체 리포지토리의 모든 커밋, 태그 및 브랜치의 그래프 보기:

`git log --oneline --decorate --all --graph`

- 특정 문자열이 포함된 커밋 메시지만 보기 (대소문자 구분 없이):

`git log -i --grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_문자열</span>

- 특정 작성자의 마지막 N개의 커밋 보기:

`git log -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">개수</span>` --author=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작성자</span>

- 두 날짜(yyyy-mm-dd) 사이의 커밋 보기:

`git log --before="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2017-01-29</span>`" --after="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2017-01-17</span>`"`
