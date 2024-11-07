---
layout: page
title: common/hg-add (한국어)
description: "지정한 파일을 Mercurial의 다음 커밋을 위한 스테이징 영역에 추가."
content_hash: ed899a64c870dfae29fff6379fb51c15b85cf8f9
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/hg-add.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hg add

지정한 파일을 Mercurial의 다음 커밋을 위한 스테이징 영역에 추가.
더 많은 정보: <https://www.mercurial-scm.org/doc/hg.1.html#add>.

- 파일 또는 디렉토리를 스테이징 영역에 추가:

`hg add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 지정된 패턴과 일치하는 모든 스테이징되지 않은 파일 추가:

`hg add --include `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>

- 지정된 패턴과 일치하지 않는 모든 스테이징되지 않은 파일 추가:

`hg add --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>

- 하위 저장소를 재귀적으로 추가:

`hg add --subrepos`

- 아무런 작업도 수행하지 않고 테스트 실행:

`hg add --dry-run`
