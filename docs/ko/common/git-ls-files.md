---
layout: page
title: common/git-ls-files (한국어)
description: "색인과 작업 트리의 파일 정보를 보여줍니다."
content_hash: 132a7770bfe56517a9f772a99c1632769fe612d6
last_modified_at: 2024-08-19
related_topics:
  - title: English version
    url: /en/common/git-ls-files.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-ls-files.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git ls-files

색인과 작업 트리의 파일 정보를 보여줍니다.
더 많은 정보: <https://git-scm.com/docs/git-ls-files>.

- 삭제된 파일 보기:

`git ls-files --deleted`

- 수정되거나 삭제된 파일 보기:

`git ls-files --modified`

- .gitignore에 명시된 파일과 Git이 관리하지 않는 파일 보기:

`git ls-files --others`

- Git이 관리하지 않는 파일 중 .gitignore에 명시되지 않은 파일 보기:

`git ls-files --others --exclude-standard`
