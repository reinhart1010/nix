---
layout: page
title: common/git-init (한국어)
description: "새로운 로컬 Git 저장소를 초기화합니다."
content_hash: 5b087c2aae0b8aaa9c5228063bf6eda9eb41b6c8
last_modified_at: 2024-06-13
related_topics:
  - title: Deutsch version
    url: /de/common/git-init.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-init.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-init.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-init.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/git-init.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-init.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-init.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-init.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git init

새로운 로컬 Git 저장소를 초기화합니다.
더 많은 정보: <https://git-scm.com/docs/git-init>.

- 새로운 로컬 저장소 초기화:

`git init`

- 초기 브랜치에 지정된 이름을 가진 저장소를 초기화:

`git init --initial-branch=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- 객체 해시로 SHA256를 사용하여 저장소 초기화 (Git 버전 2.29+ 이상 필요):

`git init --object-format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sha256</span>

- SSH를 통해 원격으로 사용할 수 있는 베어본 저장소 초기화:

`git init --bare`
