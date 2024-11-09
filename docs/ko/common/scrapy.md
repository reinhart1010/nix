---
layout: page
title: common/scrapy (한국어)
description: "웹 크롤링 프레임워크."
content_hash: f448d55002690e80bb134761a63f03b060f5bf14
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/scrapy.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/scrapy.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/scrapy.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/scrapy.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># scrapy

웹 크롤링 프레임워크.
더 많은 정보: <https://scrapy.org>.

- 프로젝트 생성:

`scrapy startproject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>

- 스파이더 생성 (프로젝트 디렉토리에서):

`scrapy genspider `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스파이더_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">웹사이트_도메인</span>

- 스파이더 편집 (프로젝트 디렉토리에서):

`scrapy edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스파이더_이름</span>

- 스파이더 실행 (프로젝트 디렉토리에서):

`scrapy crawl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스파이더_이름</span>

- Scrapy가 인식하는 방식으로 웹페이지를 가져와 `stdout`에 소스 출력:

`scrapy fetch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">URL</span>

- Scrapy가 인식하는 방식으로 웹페이지를 기본 브라우저에서 열기 (더 정확하게 보려면 JavaScript 비활성화):

`scrapy view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">URL</span>

- URL에 대한 Scrapy 셸 열기, 이 셸을 통해 Python 셸(IPython이 가능하다면)을 사용하여 페이지 소스와 상호작용 가능:

`scrapy shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">URL</span>
