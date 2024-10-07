---
layout: page
title: common/git-bulk (한국어)
description: "여러 Git 저장소에서 작업을 실행."
content_hash: db2b71e0543ebf7e1288ebd01bdfee40279d9bc4
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-bulk.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-bulk.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-bulk.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git bulk

여러 Git 저장소에서 작업을 실행.
`git-extras`의 일부.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-bulk>.

- 현재 디렉토리를 작업 공간으로 등록:

`git bulk --addcurrent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_공간_이름</span>

- 대량 작업을 위한 작업 공간 등록:

`git bulk --addworkspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_공간_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/절대/경로/대상/저장소</span>

- 특정 디렉토리 내에 저장소를 클론하고, 작업 공간으로 등록:

`git bulk --addworkspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_공간_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/절대/경로/대상/부모_디렉토리</span>` --from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_저장소_위치</span>

- 원격 위치의 새 줄로 구분된 목록에서 저장소를 클론하고, 작업 공간으로 등록:

`git bulk --addworkspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_공간_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/루트_디렉토리</span>` --from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/파일</span>

- 등록된 모든 작업 공간 나열:

`git bulk --listall`

- 현재 작업 공간의 저장소에서 Git 명령 실행:

`git bulk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령_인수</span>

- 특정 작업 공간 제거:

`git bulk --removeworkspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_공간_이름</span>

- 모든 작업 공간 제거:

`git bulk --purge`
