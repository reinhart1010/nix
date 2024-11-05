---
layout: page
title: common/nokogiri (한국어)
description: "HTML, XML, SAX 및 Reader 파서."
content_hash: 1f056f246cb6671618c8a306da01604d26f583f2
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/nokogiri.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nokogiri.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nokogiri

HTML, XML, SAX 및 Reader 파서.
더 많은 정보: <https://nokogiri.org>.

- URL 또는 파일의 내용을 파싱:

`nokogiri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|경로/대상/파일</span>

- 특정 타입으로 파싱:

`nokogiri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|경로/대상/파일</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xml|html</span>

- 파싱 전에 특정 초기화 파일 로드:

`nokogiri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|경로/대상/파일</span>` -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/설정_파일</span>

- 특정 인코딩을 사용하여 파싱:

`nokogiri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|경로/대상/파일</span>` --encoding `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인코딩</span>

- RELAX NG 파일을 사용하여 검증:

`nokogiri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|경로/대상/파일</span>` --rng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|경로/대상/파일</span>
