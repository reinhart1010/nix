---
layout: page
title: common/git-diff-index (한국어)
description: "작업 디렉터리를 커밋 또는 트리 객체와 비교."
content_hash: cd41fbf3f94428b9afadcbefbefce1dce222c045
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-diff-index.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git diff-index

작업 디렉터리를 커밋 또는 트리 객체와 비교.
더 많은 정보: <https://git-scm.com/docs/git-diff-index>.

- 작업 디렉터리를 특정 커밋과 비교:

`git diff-index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- 작업 디렉터리 내 특정 파일 또는 폴더를 커밋과 비교:

`git diff-index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 인덱스(스테이징 영역)에 있는 작업 디렉터리를 비교하여 스테이징된 변경 사항 확인:

`git diff-index --cached `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- 출력 억제 및 종료 상태를 반환하여 차이점 확인:

`git diff-index --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
