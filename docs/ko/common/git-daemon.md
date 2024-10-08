---
layout: page
title: common/git-daemon (한국어)
description: "Git 저장소를 위한 매우 간단한 서버."
content_hash: d90d626e096d01189fd085547cf1025b9327bba2
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-daemon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git daemon

Git 저장소를 위한 매우 간단한 서버.
더 많은 정보: <https://git-scm.com/docs/git-daemon>.

- 허용된 디렉토리 집합으로 Git 데몬 실행:

`git daemon --export-all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더2</span>

- 특정 기본 디렉토리로 Git 데몬 실행하고 Git 저장소처럼 보이는 모든 하위 디렉토리에서 조회 허용:

`git daemon --base-path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --export-all --reuseaddr`

- 지정된 디렉토리에서 Git 데몬을 실행하여 로그 메시지를 자세히 출력하고 Git 클라이언트가 쓸 수 있도록 허용:

`git daemon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --enable=receive-pack --informative-errors --verbose`
