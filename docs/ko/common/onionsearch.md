---
layout: page
title: common/onionsearch (한국어)
description: "다양한 `.onion` 검색 엔진에서 URL을 스크랩."
content_hash: 9938054d43708a5f985e1cb650fd0eb86f1b14a4
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/onionsearch.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/onionsearch.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># onionsearch

다양한 `.onion` 검색 엔진에서 URL을 스크랩.
참고: `onionsearch`는 `localhost:9050`에서 실행되는 Tor 프록시가 필요하며, `.onion` 웹사이트를 방문하려면 Tor 지원 브라우저가 필요합니다.
더 많은 정보: <https://github.com/megadose/OnionSearch>.

- 모든 검색 엔진에서 결과 요청:

`onionsearch "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`"`

- 특정 검색 엔진에서 검색 결과 요청:

`onionsearch "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`" --engines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tor66 deeplink phobos ...</span>

- 검색 시 특정 검색 엔진 제외:

`onionsearch "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`" --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">candle ahmia ...</span>

- 엔진당 로드할 페이지 수 제한:

`onionsearch "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stuxnet</span>`" --engines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tor66 deeplink phobos ...</span>` --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- 지원되는 모든 검색 엔진 나열:

`onionsearch --help | grep -A1 -i "supported engines"`
