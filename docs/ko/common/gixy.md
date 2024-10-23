---
layout: page
title: common/gixy (한국어)
description: "nginx 구성 파일 분석."
content_hash: b4d07045e909f2d5f44db8adf1356efebc4a5b52
last_modified_at: 2024-10-23
related_topics:
  - title: English version
    url: /en/common/gixy.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gixy.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gixy

nginx 구성 파일 분석.
더 많은 정보: <https://github.com/yandex/gixy>.

- nginx 구성 파일 분석 (기본 경로: `/etc/nginx/nginx.conf`):

`gixy`

- nginx 구성 분석하지만 특정 테스트 넘어감:

`gixy --skips `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http_splitting</span>

- 특정 세부 수준으로 nginx 구성을 분석:

`gixy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|-ll|-lll</span>

- 특정 경로에서 nginx 구성 파일을 분석:

`gixy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성_파일_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성_파일_2</span>
