---
layout: page
title: common/hub (한국어)
description: "GitHub 기반 프로젝트 작업을 위한 명령을 추가하는 Git용 래퍼."
content_hash: bbd0065b880130bbf50c419ba4aeafe2b8a9e3ce
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/hub.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hub

GitHub 기반 프로젝트 작업을 위한 명령을 추가하는 Git용 래퍼.
`hub alias`의 지시에 따라 설정되면, `git`을 사용하여 `hub` 명령을 실행할 수 있음.
더 많은 정보: <https://hub.github.com>.

- slug를 사용해 저장소를 복제 (소유자는 사용자 이름을 생략할 수 있음):

`hub clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_이름</span>

- GitHub 프로필 아래에 현재 저장소 (다른 사용자로부터 복제됨)의 포크를 생성:

`hub fork`

- 현재 로컬 브랜치를 GitHub에 푸시하고 원본 저장소에 이에 대한 PR을 생성:

`hub push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>` && hub pull-request`

- 첫 번째 커밋의 메시지를 재사용하여 현재 (이미 푸시된) 브랜치의 PR을 생성:

`hub pull-request --no-edit`

- 풀 요청 내용으로 새 브랜치를 생성하고, 해당 브랜치로 전환:

`hub pr checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_번호</span>

- 현재 (로컬 전용) 저장소를 GitHub 계정에 업로드:

`hub create`

- 업스트림에서 Git 객체를 가져오고 로컬 브랜치를 업데이트:

`hub sync`
