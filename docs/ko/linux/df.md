---
layout: page
title: linux/df (한국어)
description: "파일 시스템 디스크 공간 사용 개요를 표시합니다."
content_hash: 31e5a82261402b1220e4dafafc8fdac364975340
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/df.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/linux/df.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/df.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/df.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/df.html
    icon: bi bi-globe
tldri18n_status: 2
---
# df

파일 시스템 디스크 공간 사용 개요를 표시합니다.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/df-invocation.html>.

- 모든 파일 시스템과 디스크 사용량 표시:

`df`

- 모든 파일 시스템과 디스크 사용량을 사람이 읽기 쉬운 형식으로 표시:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--human-readable</span>

- 주어진 파일 또는 디렉토리를 포함하는 파일 시스템과 디스크 사용량 표시:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 사용 가능한 inode 수에 대한 통계 포함:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--inodes</span>

- 특정 유형을 제외한 파일 시스템 표시:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-x|--exclude-type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">squashfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-x|--exclude-type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs</span>

- 파일 시스템 유형 표시:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-T|--print-type</span>
