---
layout: page
title: common/difft (한국어)
description: "프로그래밍 언어의 구문을 기반으로 파일이나 디렉터리를 비교."
content_hash: 4ad9ca7ec8d3984a7f886356bb7013e1cda82389
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/difft.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/difft.html
    icon: bi bi-globe
tldri18n_status: 2
---
# difft

프로그래밍 언어의 구문을 기반으로 파일이나 디렉터리를 비교.
참고: `delta`, `diff`.
더 많은 정보: <https://difftastic.wilfred.me.uk/introduction.html>.

- 두 개의 파일 또는 디렉터리를 비교:

`difft `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리2</span>

- 파일 간의 차이점만 보고:

`difft --check-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>

- 디스플레이 모드를 지정 (기본값은 `side-by-side`):

`difft --display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">side-by-side|side-by-side-show-both|inline|json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>

- 비교할 때 설명을 무시:

`difft --ignore-comments `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>

- 소스코드 구문 강조 활성화/비활성화 (기본값은 `on`):

`difft --syntax-highlight `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>

- 파일 간에 차이가 없으면 아무것도 출력하지 않음:

`difft --skip-unchanged `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리2</span>

- 확장명과 함께, 도구에서 지원하는 모든 프로그래밍 언어를 출력:

`difft --list-languages`
