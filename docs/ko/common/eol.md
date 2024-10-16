---
layout: page
title: common/eol (한국어)
description: "여러 제품의 수명 종료 날짜(EoL)를 표시."
content_hash: c145840bb3cc3fdad18ae8751ed9e60d815a6dae
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/eol.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/eol.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># eol

여러 제품의 수명 종료 날짜(EoL)를 표시.
더 많은 정보: <https://github.com/hugovk/norwegianblue>.

- 사용 가능한 모든 제품의 목록을 나열:

`eol`

- 하나 이상의 제품에 대한 EoL을 가져옴:

`eol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제품1 제품2 ...</span>

- 제품 웹페이지 열기:

`eol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제품</span>` --web`

- 특정 형식으로 하나 이상의 제품에 대한 EoL을 가져옴노:

`eol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제품1 제품2 ...</span>` --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html|json|md|markdown|pretty|rst|csv|tsv|yaml</span>

- 하나 이상의 제품에 대한 EoL을 단일 마크다운 파일로 가져옴:

`eol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제품1 제품2 ...</span>` --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">마크다운</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eol_보고서.md</span>

- 도움말 표시:

`eol --help`
