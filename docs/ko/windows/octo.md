---
layout: page
title: windows/octo (한국어)
description: "Octopus Deploy 명령줄 도구."
content_hash: f69aebf3f257a88b85ab3ed347d819c4e7bdbd8e
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/windows/octo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# octo

Octopus Deploy 명령줄 도구.
더 많은 정보: <https://octopus.com/docs/octopus-rest-api/octo.exe-command-line>.

- 패키지 생성:

`octo pack --id=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지를 Octopus 서버의 저장소에 푸시:

`octo push --package=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 릴리스 생성:

`octo create-release --project=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>` --packageversion=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 릴리스 배포:

`octo deploy-release --project=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>` --packageversion=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>` --deployto=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">환경_이름</span>` --tenant=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">배포_대상</span>
