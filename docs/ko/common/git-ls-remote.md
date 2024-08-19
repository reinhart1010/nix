---
layout: page
title: common/git-ls-remote (한국어)
description: "원격 저장소의 브랜치, 태그 등의 정보를 나열하는 Git 명령어입니다."
content_hash: 6c090c0f3230ac0a1b6fece34345cafd93f17b56
last_modified_at: 2024-08-19
related_topics:
  - title: English version
    url: /en/common/git-ls-remote.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-ls-remote.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-ls-remote.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-ls-remote.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git ls-remote

원격 저장소의 브랜치, 태그 등의 정보를 나열하는 Git 명령어입니다.
이름이나 URL이 주어지지 않으면 설정된 업스트림 브랜치를 사용하며, 업스트림이 설정되지 않은 경우 원격 origin을 사용합니다.
더 많은 정보: <https://git-scm.com/docs/git-ls-remote>.

- 기본 원격 저장소의 모든 브랜치와 태그 정보 보기:

`git ls-remote`

- 기본 원격 저장소의 브랜치 정보만 보기:

`git ls-remote --heads`

- 기본 원격 저장소의 태그 정보만 보기:

`git ls-remote --tags`

- 이름이나 URL을 기반으로 특정 원격 저장소의 모든 브랜치와 태그 정보 보기:

`git ls-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_URL</span>

- 특정 검색어와 일치하는 정보만 보기:

`git ls-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_이름</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_혹은_태그_이름</span>`"`
