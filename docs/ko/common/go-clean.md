---
layout: page
title: common/go-clean (한국어)
description: "오브젝트 파일과 캐시 파일 제거."
content_hash: aa68c31d4cb22e6e394271f77f4c5a39e5d7e42e
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/common/go-clean.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/go-clean.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/go-clean.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go clean

오브젝트 파일과 캐시 파일 제거.
더 많은 정보: <https://golang.org/cmd/go/#hdr-Remove_object_files_and_cached_files>.

- 실제로 제거하지 않고 제거 명령 출력:

`go clean -n`

- 빌드 캐시 삭제:

`go clean -cache`

- 모든 캐시된 테스트 결과 삭제:

`go clean -testcache`

- 모듈 캐시 삭제:

`go clean -modcache`
