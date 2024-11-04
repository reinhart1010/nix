---
layout: page
title: common/vidir (한국어)
description: "텍스트 편집기에서 디렉터리를 편집."
content_hash: 46913d96116d2a7f382b67db0abcd96e4149ac1d
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/vidir.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vidir

텍스트 편집기에서 디렉터리를 편집.
더 많은 정보: <https://joeyh.name/code/moreutils/>.

- 지정된 디렉터리의 내용을 편집:

`vidir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리1 경로/대상/디렉터리2 ...</span>

- 프로그램에서 수행한 각 작업을 표시:

`vidir --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리1 경로/대상/디렉터리2 ...</span>

- 현재 디렉터리의 내용을 편집:

`vidir`

- 지정된 텍스트 편집기를 사용:

`EDITOR=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vim</span>` vidir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리1 경로/대상/디렉터리2 ...</span>

- `stdin`에서 편집할 파일 목록을 읽기:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | vidir -`
