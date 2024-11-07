---
layout: page
title: common/lighthouse (한국어)
description: "웹 애플리케이션과 웹 페이지를 분석하여 최신 성능 메트릭과 개발자 모범 사례에 대한 통찰을 수집합니다."
content_hash: 2ce32f1b3a23557ce35f87ee685345f14a4b8e75
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/lighthouse.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/lighthouse.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lighthouse

웹 애플리케이션과 웹 페이지를 분석하여 최신 성능 메트릭과 개발자 모범 사례에 대한 통찰을 수집합니다.
더 많은 정보: <https://github.com/GoogleChrome/lighthouse>.

- 특정 웹사이트에 대한 HTML 보고서를 생성하고 현재 디렉토리에 파일로 저장:

`lighthouse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- JSON 보고서를 생성하고 출력:

`lighthouse --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- JSON 보고서를 생성하고 특정 파일에 저장:

`lighthouse --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json</span>` --output-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- 브라우저를 무헤드 모드로 사용하고 `stdout`에 기록하지 않고 보고서 생성:

`lighthouse --quiet --chrome-flags="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--headless</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- 모든 요청에 대해 지정된 JSON 파일의 HTTP 헤더 키/값 쌍을 사용하여 보고서 생성:

`lighthouse --extra-headers=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- 특정 카테고리만을 위한 보고서 생성:

`lighthouse --only-categories=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">performance,accessibility,best-practices,seo,pwa</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- 장치 에뮬레이션과 모든 제한을 비활성화하여 보고서 생성:

`lighthouse --screenEmulation.disabled --throttling-method=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">provided</span>` --no-emulatedUserAgent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- 도움말 표시:

`lighthouse --help`
