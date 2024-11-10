---
layout: page
title: linux/pkgctl-repo (한국어)
description: "Arch Linux용 Git 패키징 저장소 및 구성 관리."
content_hash: ec730202994a6128d5e42f5550b970345e0eb752
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/pkgctl-repo.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/pkgctl-repo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkgctl repo

Arch Linux용 Git 패키징 저장소 및 구성 관리.
같이 보기: `pkgctl`.
더 많은 정보: <https://manned.org/pkgctl-repo.1>.

- 패키지 저장소를 클론(Arch Linux GitLab 계정에 SSH 키 설정 필요):

`pkgctl repo clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지명</span>

- HTTPS를 통해 패키지 저장소를 클론:

`pkgctl repo clone --protocol=https `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지명</span>

- 새로운 GitLab 패키지 저장소 생성 후 클론(GitLab API 인증 필요):

`pkgctl repo create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_기본명</span>

- 특정 버전으로 패키지 저장소 전환:

`pkgctl repo switch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_기본명</span>

- 패키지 저장소의 웹사이트 열기:

`pkgctl repo web `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_기본명</span>
