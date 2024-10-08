---
layout: page
title: common/git-magic (한국어)
description: "추가, 커밋 및 푸시 루틴 자동화."
content_hash: 96f0ca6eb289f9e85281238b5245417f6c90eef9
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-magic.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git magic

추가, 커밋 및 푸시 루틴 자동화.
`git-extras`의 일부.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-magic>.

- 생성된 메시지로 변경 사항 커밋:

`git magic`

- 추적되지 않은 파일을 [a]dd하고 생성된 메시지로 변경 사항 커밋:

`git magic -a`

- 사용자 정의 [m]essage로 변경 사항 커밋:

`git magic -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_커밋_메시지</span>`"`

- 커밋하기 전에 커밋 [m]essage를 [e]dit:

`git magic -em "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_커밋_메시지</span>`"`

- 변경 사항 커밋 및 원격 저장소에 [p]ush:

`git magic -p`

- 변경 사항 커밋 및 원격 저장소에 [f]orce [p]ush:

`git magic -fp`
