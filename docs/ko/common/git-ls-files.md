---
layout: page
title: common/git-ls-files (한국어)
description: "색인과 작업 트리의 파일 정보를 보여줍니다."
content_hash: 4ae6d9ff4635905cc7d92ed87f985e9aa51b36b4
last_modified_at: 2024-08-12
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
더 자세한 정보: <https://git-scm.com/docs/git-ls-files>.

- 삭제된 파일 보기:

`git ls-files --deleted`

- 수정되거나 삭제된 파일 보기:

`git ls-files --modified`

- .gitignore에 명시된 파일과 Git이 관리하지 않는 파일 보기:

`git ls-files --others`

- Git이 관리하지 않는 파일 중 .gitignore에 명시되지 않은 파일 보기:

`git ls-files --others --exclude-standard`
