---
layout: page
title: common/cbt (한국어)
description: "Google Cloud's Bigtable에서 데이터를 읽는 유틸리티."
content_hash: 719eda840c37fe59b8ed96b1c67ca608adb8cc3b
last_modified_at: 2024-09-30
related_topics:
  - title: English version
    url: /en/common/cbt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cbt

Google Cloud's Bigtable에서 데이터를 읽는 유틸리티.
더 많은 정보: <https://cloud.google.com/bigtable/docs/cbt-reference>.

- 현재 프로젝트의 테이블 나열:

`cbt ls`

- 현재 프로젝트의 특정 테이블에 있는 행 수를 인쇄:

`cbt count "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블_이름</span>`"`

- 현재 프로젝트의 열 당 1개의 (가장 최근) 셀 수정만 사용하여 특정 테이블의 단일 행을 표시:

`cbt lookup "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블_이름</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">열_키</span>`" cells-per-column=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- 현재 프로젝트에서 특정 열만 있는 단일 행 표시 (전체 패밀리를 반환하려면 한정자를 생략):

`cbt lookup "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블_이름</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">열_키</span>`" columns="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">family1:qualifier1,family2:qualifier2,...</span>`"`

- 특정 정규식 패턴으로 현재 프로젝트에서 최대 5개 행을 검색하고 인쇄:

`cbt read "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블_이름</span>`" regex="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">열_키_패턴</span>`" count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- 특정 행 범위를 읽고, 현재 프로젝트에서 반환된 행 키만 인쇄:

`cbt read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블_이름</span>` start=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시작_열_키</span>` end=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">마지막_열_키</span>` keys-only=true`
