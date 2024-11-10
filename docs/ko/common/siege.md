---
layout: page
title: common/siege (한국어)
description: "HTTP 부하 테스트 및 벤치마킹 도구."
content_hash: a039978667d7428be784732be9c40b15440b1121
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/siege.html
    icon: bi bi-globe
tldri18n_status: 2
---
# siege

HTTP 부하 테스트 및 벤치마킹 도구.
더 많은 정보: <https://www.joedog.org/siege-manual/>.

- 기본 설정으로 URL 테스트:

`siege `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- URL 목록 테스트:

`siege --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/url_목록.txt</span>

- URL 목록을 무작위 순서로 테스트 (인터넷 트래픽 시뮬레이션):

`siege --internet --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/url_목록.txt</span>

- URL 목록 벤치마킹 (요청 사이에 대기하지 않음):

`siege --benchmark --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/url_목록.txt</span>

- 동시 연결 수 설정:

`siege --concurrent=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/url_목록.txt</span>

- 실행 시간 설정:

`siege --time=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30s</span>` --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/url_목록.txt</span>
