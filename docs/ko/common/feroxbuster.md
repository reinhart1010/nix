---
layout: page
title: common/feroxbuster (한국어)
description: "Rust로 작성된 간단하고 빠르며 반복적인 콘텐츠 검색 도구."
content_hash: 865339f81741149ce3fa5935292d88889d62e503
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/feroxbuster.html
    icon: bi bi-globe
tldri18n_status: 2
---
# feroxbuster

Rust로 작성된 간단하고 빠르며 반복적인 콘텐츠 검색 도구.
웹 서버 등에서 숨겨진 경로를 무차별 공격하는 데 사용됨.
더 많은 정보: <https://epi052.github.io/feroxbuster-docs/docs/>.

- 확장자, 100개의 스레드 및 임의의 사용자 에이전트가 포함된 단어 목록에서 일치하는 특정 디렉터리 및 파일 검색:

`feroxbuster --url "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>`" --wordlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` --threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --extensions "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php,txt</span>`" --random-agent`

- 특정 프록시를 통해 재귀 없이 디렉터리를 열거:

`feroxbuster --url "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>`" --wordlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` --no-recursion --proxy "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://127.0.0.1:8080</span>`"`

- 웹페이지에서 링크 찾기:

`feroxbuster --url "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>`" --extract-links`

- 특정 상태 코드 및 문자 수로 필터링:

`feroxbuster --url "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>`" --filter-status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">301</span>` --filter-size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4092</span>
