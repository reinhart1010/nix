---
layout: page
title: common/git-restore (한국어)
description: "작업 트리 파일을 복원합니다. Git 버전 2.23+ 이상이 필요합니다."
content_hash: 8f42e9d49b32ca6b92056b20ab1b81073b5b23a5
last_modified_at: 2024-06-12
related_topics:
  - title: English version
    url: /en/common/git-restore.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-restore.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-restore.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-restore.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-restore.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-restore.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git restore

작업 트리 파일을 복원합니다. Git 버전 2.23+ 이상이 필요합니다.
같이 보기: `git checkout` 및 `git reset`.
더 많은 정보: <https://git-scm.com/docs/git-restore>.

- 언스테이지된 파일을 현재 커밋 (HEAD)의 버전으로 복원:

`git restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 언스테이지된 파일을 특정 커밋의 버전으로 복원:

`git restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 추적 중인 파일에 대한 모든 언스테이지된 변경 사항을 폐기:

`git restore :/`

- 파일의 스테이지를 내리기:

`git restore --staged `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 모든 파일의 스테이지를 내리기:

`git restore --staged :/`

- 스테이지 및 언스테이지된 파일의 모든 변경 사항 폐기:

`git restore --worktree --staged :/`

- 파일의 섹션을 대화적으로 선택하여 복원:

`git restore --patch`
