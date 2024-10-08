---
layout: page
title: common/git-guilt (한국어)
description: "스테이지되지 않은 변경 사항이 있는 파일에 대한 전체 블레임 수를 표시하거나 두 개의 리비전 간 블레임 변경을 계산."
content_hash: eb3befaa61f27768c485662f72c941e1639ee3a1
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-guilt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git guilt

스테이지되지 않은 변경 사항이 있는 파일에 대한 전체 블레임 수를 표시하거나 두 개의 리비전 간 블레임 변경을 계산.
`git-extras`의 일부.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-guilt>.

- 전체 블레임 수 표시:

`git guilt`

- 두 개의 리비전 간 블레임 변경 계산:

`git guilt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">첫번째_리비전</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">마지막_리비전</span>

- 작성자 이메일을 이름 대신 표시:

`git guilt --email`

- 블레임을 할당할 때 공백만 변경된 부분 무시:

`git guilt --ignore-whitespace`

- 지난 3주 동안의 블레임 델타 찾기:

`git guilt 'git log --until="3 weeks ago" --format="%H" -n 1'`

- 지난 3주 동안의 블레임 델타 찾기 (git 1.8.5+):

`git guilt @{3.weeks.ago}`
