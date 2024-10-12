---
layout: page
title: common/ctags (한국어)
description: "널리 사용되는 많은 프로그래밍 언어에 대해 소스 파일에 있는 언어 객체의 인덱스 (또는 태그) 파일을 생성."
content_hash: d453b7d34c5bd5561f47c0188a9b2779f827dd19
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/ctags.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ctags

널리 사용되는 많은 프로그래밍 언어에 대해 소스 파일에 있는 언어 객체의 인덱스 (또는 태그) 파일을 생성.
더 많은 정보: <https://ctags.io/>.

- 단일 파일에 대한 태그를 생성하고, 현재 디렉터리에 "tags"라는 파일로 출력, 파일이 존재하면 덮어씀:

`ctags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 현재 디렉터리의 모든 파일에 대한 태그를 생성하고, 특정 파일에 출력, 파일이 존재하면 덮어씀:

`ctags -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` *`

- 현재 디렉터리와 모든 하위 디렉터리의 모든 파일에 대한 태그를 생성:

`ctags --recurse`

- 단일 파일에 대한 태그를 생성하고, JSON 형식의 시작 줄 번호와 끝 줄 번호로 출력:

`ctags --fields=+ne --output-format=json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
