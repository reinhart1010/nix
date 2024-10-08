---
layout: page
title: common/git-commit (한국어)
description: "파일을 저장소에 커밋합니다."
content_hash: ec02c65cca4973cb5495eabfbe9391c650d64e7f
last_modified_at: 2024-10-07
related_topics:
  - title: Deutsch version
    url: /de/common/git-commit.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-commit.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-commit.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-commit.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-commit.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-commit.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/git-commit.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-commit.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-commit.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-commit.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-commit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git commit

파일을 저장소에 커밋합니다.
더 많은 정보: <https://git-scm.com/docs/git-commit>.

- 스테이징된 파일을 메시지와 함께 저장소에 커밋:

`git commit --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`"`

- 파일에서 읽은 메시지로 스테이징된 파일을 저장소에 커밋:

`git commit --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/커밋_메시지_파일</span>

- 수정 및 삭제된 모든 파일을 자동으로 스테이징하고 메시지와 함께 커밋:

`git commit --all --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`"`

- 스테이징된 파일을 커밋하고 지정된 GPG 키로 서명합니다 (인수가 지정되지 않은 경우 구성 파일에 정의된 키 사용):

`git commit --gpg-sign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_아이디</span>` --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`"`

- 현재 스테이징된 변경 사항을 추가하여 마지막 커밋을 업데이트하고 커밋의 해시를 변경합니다:

`git commit --amend`

- 특정 파일(이미 스테이징된)만 커밋:

`git commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 스테이징된 파일이 없더라도 커밋 생성:

`git commit --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`" --allow-empty`
