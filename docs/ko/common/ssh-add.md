---
layout: page
title: common/ssh-add (한국어)
description: "`ssh-agent`에서 로드된 SSH 키를 관리."
content_hash: 229c0fd4759b3de00d42135f99d267e0fb8e4906
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/ssh-add.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ssh-add.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ssh-add.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ssh-add.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ssh-add

`ssh-agent`에서 로드된 SSH 키를 관리.
키가 로드되도록 `ssh-agent`가 실행 중인지 확인하세요.
더 많은 정보: <https://man.openbsd.org/ssh-add>.

- 기본 SSH 키를 `~/.ssh`에서 ssh-agent로 추가:

`ssh-add`

- 특정 키를 ssh-agent로 추가:

`ssh-add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/개인_키</span>

- 현재 로드된 키의 지문 나열:

`ssh-add -l`

- ssh-agent에서 키 삭제:

`ssh-add -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/개인_키</span>

- 현재 로드된 모든 키를 ssh-agent에서 삭제:

`ssh-add -D`

- 키를 ssh-agent와 키체인에 추가:

`ssh-add -K `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/개인_키</span>
