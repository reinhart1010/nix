---
layout: page
title: common/git-gui (한국어)
description: "Git의 GUI를 사용하여 브랜치, 커밋, 원격 저장소를 관리하고 로컬 병합을 수행할 수 있습니다."
content_hash: 2af2518dd071bfd2e76d85573b6c3b33652cda8f
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-gui.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-gui.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-gui.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git gui

Git의 GUI를 사용하여 브랜치, 커밋, 원격 저장소를 관리하고 로컬 병합을 수행할 수 있습니다.
같이 보기: `git-cola`, `gitk`.
더 많은 정보: <https://git-scm.com/docs/git-gui>.

- GUI 시작:

`git gui`

- 각 줄에 작성자 이름과 커밋 해시가 표시된 특정 파일 보기:

`git gui blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 리비전에서 `git gui blame` 열기:

`git gui blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리비전</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 줄을 중심으로 뷰를 스크롤하여 `git gui blame` 열기:

`git gui blame --line=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">줄</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 하나의 커밋을 만들기 위한 창을 열고 완료되면 쉘로 돌아가기:

`git gui citool`

- "마지막 커밋 수정" 모드로 `git gui citool` 열기:

`git gui citool --amend`

- 읽기 전용 모드로 `git gui citool` 열기:

`git gui citool --nocommit`

- 특정 브랜치의 트리 브라우저를 열고, 파일을 클릭하면 블레임 도구 열기:

`git gui browser maint`
