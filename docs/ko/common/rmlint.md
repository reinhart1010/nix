---
layout: page
title: common/rmlint (한국어)
description: "파일 시스템에서 공간 낭비 및 기타 손상된 항목을 찾습니다."
content_hash: f941921625236663392824d4b4fd4af217fdf6a2
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/rmlint.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rmlint

파일 시스템에서 공간 낭비 및 기타 손상된 항목을 찾습니다.
더 많은 정보: <https://rmlint.readthedocs.io/en/latest/rmlint.1.html>.

- 중복, 빈 파일 및 손상된 파일에 대해 디렉토리를 검사:

`rmlint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리1 경로/대상/디렉토리2 ...</span>

- 공간 낭비 항목을 검사하며, 태그된 디렉토리에 파일을 유지 (더블 슬래시 이후):

`rmlint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>` // `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본_디렉토리</span>

- 태그가 없는 디렉토리에 모든 파일을 유지하며 공간 낭비 항목 검사:

`rmlint --keep-all-untagged `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>` // `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본_디렉토리</span>

- `rmlint` 실행으로 발견된 중복 파일 삭제:

`./rmlint.sh`

- 중복된 디렉토리 트리 찾기:

`rmlint --merge-directories `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>

- [d] 경로 깊이가 낮은 파일을 원본으로 표시하고, 동률일 경우 더 짧은 [l] 길이 선택:

`rmlint --rank-by=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>

- 동일한 내용 외에도 동일한 파일 이름을 가진 중복 항목만 찾기:

`rmlint --match-basename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>

- 동일한 내용 외에도 동일한 확장자를 가진 중복 항목만 찾기:

`rmlint --match-extension `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>
