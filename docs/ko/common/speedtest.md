---
layout: page
title: common/speedtest (한국어)
description: "https://speedtest.net을 사용하여 인터넷 대역폭을 테스트하는 공식 명령줄 인터페이스."
content_hash: 83f56b4fb32353e7cbdb5ac35c8a187b6c2c61f8
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/speedtest.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/speedtest.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># speedtest

https://speedtest.net을 사용하여 인터넷 대역폭을 테스트하는 공식 명령줄 인터페이스.
참고: 일부 플랫폼에서는 `speedtest`를 `speedtest-cli`에 연결합니다. 이 페이지의 일부 예제가 작동하지 않는 경우, `speedtest-cli`를 참조하세요.
더 많은 정보: <https://www.speedtest.net/apps/cli>.

- 속도 테스트 실행:

`speedtest`

- 속도 테스트를 실행하고 출력 단위를 지정:

`speedtest --unit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">auto-decimal-bits|auto-decimal-bytes|auto-binary-bits|auto-binary-bytes</span>

- 속도 테스트를 실행하고 출력 형식을 지정:

`speedtest --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">human-readable|csv|tsv|json|jsonl|json-pretty</span>

- 속도 테스트를 실행하고 소수점 자릿수를 지정 (0에서 8까지, 기본값은 2):

`speedtest --precision=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정밀도</span>

- 속도 테스트를 실행하고 진행 상황을 출력 (출력 형식이 `human-readable` 및 `json`일 때만 사용 가능):

`speedtest --progress=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yes|no</span>

- 거리에 따라 정렬된 모든 `speedtest.net` 서버 나열:

`speedtest --servers`

- 특정 `speedtest.net` 서버로 속도 테스트 실행:

`speedtest --server-id=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_ID</span>
