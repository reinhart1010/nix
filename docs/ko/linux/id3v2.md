---
layout: page
title: linux/id3v2 (한국어)
description: "id3v2 태그를 관리하고 id3v1을 변환 및 나열합니다."
content_hash: 1667fe33456ab41878bede8b7ba5f8efb4861e21
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/id3v2.html
    icon: bi bi-globe
tldri18n_status: 2
---
# id3v2

id3v2 태그를 관리하고 id3v1을 변환 및 나열합니다.
더 많은 정보: <https://manned.org/id3v2.1>.

- 모든 장르 나열:

`id3v2 --list-genres`

- 특정 파일의 모든 태그 나열:

`id3v2 --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 특정 파일의 `id3v2` 또는 `id3v1` 태그 모두 삭제:

`id3v2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--delete-v2|--delete-v1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 도움말 표시:

`id3v2 --help`

- 버전 표시:

`id3v2 --version`
