---
layout: page
title: common/hg-clone (한국어)
description: "기존 저장소의 복사본을 새 디렉터리에 생성."
content_hash: 7671048d2a97f2a7dafbb5cfd24605a27ac94a63
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/hg-clone.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hg clone

기존 저장소의 복사본을 새 디렉터리에 생성.
더 많은 정보: <https://www.mercurial-scm.org/doc/hg.1.html#clone>.

- 저장소를 지정한 디렉터리에 클론:

`hg clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_저장소_소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_경로</span>

- 특정 브랜치의 헤드로 저장소를 클론하고 이후 커밋 무시:

`hg clone --branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_저장소_소스</span>

- 파일을 체크아웃하지 않고 `.hg` 디렉터리만으로 저장소를 클론:

`hg clone --noupdate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_저장소_소스</span>

- 특정 리비전, 태그 또는 브랜치로 저장소를 클론하며 전체 기록 유지:

`hg clone --updaterev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리비전</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_저장소_소스</span>

- 특정 리비전까지만 저장소를 클론하고 이후 기록 무시:

`hg clone --rev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리비전</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_저장소_소스</span>
