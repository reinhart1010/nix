---
layout: page
title: common/cradle-install (한국어)
description: "Cradle PHP 프레임워크 구성 요소를 설치."
content_hash: f0bae7d9ca96ec2081445810a20bbbe764aed6c6
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/cradle-install.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cradle-install.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cradle-install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cradle install

Cradle PHP 프레임워크 구성 요소를 설치.
더 많은 정보: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#install>.

- Cradle의 구성요소 설치 (유저는 자세한 내용을 묻는 메시지를 받음):

`cradle install`

- 파일을 강제로 덮어 쓰기:

`cradle install --force`

- 실행중인 SQL 마이그레이션 건너 뛰기:

`cradle install --skip-sql`

- 실행중인 패키지 업데이트 건너 뛰기:

`cradle install --skip-versioning`

- 특정 데이터베이스 세부 사항 사용:

`cradle install -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">유저명</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>
