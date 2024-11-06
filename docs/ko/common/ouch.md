---
layout: page
title: common/ouch (한국어)
description: "파일 및 디렉터리를 압축하고 해제하는 명령줄 유틸리티."
content_hash: 7fbed579c3dbf07ca5c8fb891d0faf8824c83956
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ouch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ouch

파일 및 디렉터리를 압축하고 해제하는 명령줄 유틸리티.
더 많은 정보: <https://crates.io/crates/ouch>.

- 특정 파일 압축 해제:

`ouch decompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.tar.xz</span>

- 특정 위치에 파일 압축 해제:

`ouch decompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.tar.xz</span>` --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 여러 파일 압축 해제:

`ouch decompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브1.tar 경로/대상/아카이브2.tar.gz ...</span>

- 파일 압축:

`ouch compress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.zip</span>
