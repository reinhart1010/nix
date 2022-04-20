---
layout: page
title: common/git-cherry-pick (한국어)
description: "기존의 커밋에서 가져온 변경내용을 현재 브랜치에 적용합니다."
content_hash: 5d5682b3f24529ef3f3e5ae90530a564959ebf4e
related_topics:
  - title: বাংলা version
    url: /bn/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-cherry-pick.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git cherry-pick

기존의 커밋에서 가져온 변경내용을 현재 브랜치에 적용합니다.
변경내용을 다른 브랜치에 적용하고싶으면, 우선 `git checkout`을 사용해 원하는 브랜치로 변경하세요.
더 많은 정보: <https://git-scm.com/docs/git-cherry-pick>.

- 커밋을 현재 브랜치에 적용:

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋</span>

- 특정 범위의 커밋들을 현재 브랜치에 적용 (`git rebase --onto`도 보세요):

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시작_커밋</span>`~..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">끝_커밋</span>

- 연속되지 않은 여러 커밋들을 현재 브랜치에 적용:

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋_2</span>

- 커밋의 변경내역을 커밋 없이 디렉토리에 추가:

`git cherry-pick -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋</span>
