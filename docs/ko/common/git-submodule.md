---
layout: page
title: common/git-submodule (한국어)
description: "서브모듈을 검사하고 업데이트하며 관리합니다."
content_hash: 53be8c02e90b117ac31c3135efd93f45343d5d6d
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-submodule.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-submodule.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-submodule.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-submodule.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-submodule.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git submodule

서브모듈을 검사하고 업데이트하며 관리합니다.
더 많은 정보: <https://git-scm.com/docs/git-submodule>.

- 저장소의 지정된 서브모듈 설치:

`git submodule update --init --recursive`

- Git 저장소를 서브모듈로 추가:

`git submodule add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_url</span>

- Git 저장소를 지정된 폴더에 서브모듈로 추가:

`git submodule add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_url</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 모든 서브모듈을 최신 커밋으로 업데이트:

`git submodule foreach git pull`
