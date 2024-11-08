---
layout: page
title: common/pigz (한국어)
description: "멀티스레드 zlib 압축 유틸리티."
content_hash: cfc155594c4ff776e682388df05e9921fdffa144
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/pigz.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pigz

멀티스레드 zlib 압축 유틸리티.
더 많은 정보: <https://github.com/madler/pigz>.

- 파일을 기본 옵션으로 압축:

`pigz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 최상의 압축 방법으로 파일 압축:

`pigz -9 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 압축 없이 4개의 프로세서를 사용하여 파일 압축:

`pigz -0 -p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 디렉터리를 tar로 압축:

`tar cf - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` | pigz > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.tar.gz</span>

- 파일 압축 해제:

`pigz -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아카이브.gz</span>

- 아카이브의 내용 목록:

`pigz -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아카이브.tar.gz</span>
