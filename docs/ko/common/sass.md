---
layout: page
title: common/sass (한국어)
description: "SCSS 또는 Sass 파일을 CSS로 변환."
content_hash: f08d6d3ad71ada4c793f3f28852907e312cbc029
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sass.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/sass.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sass.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sass

SCSS 또는 Sass 파일을 CSS로 변환.
더 많은 정보: <https://sass-lang.com/documentation/cli/dart-sass>.

- SCSS 또는 Sass 파일을 CSS로 변환하고 결과를 출력:

`sass `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력파일.scss|입력파일.sass</span>

- SCSS 또는 Sass 파일을 CSS로 변환하고 결과를 파일에 저장:

`sass `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력파일.scss|입력파일.sass</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력파일.css</span>

- SCSS 또는 Sass 파일의 변경사항을 감시하고 동일한 파일명으로 CSS 파일 출력 또는 업데이트:

`sass --watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력파일.scss|입력파일.sass</span>

- SCSS 또는 Sass 파일의 변경사항을 감시하고 주어진 파일명으로 CSS 파일 출력 또는 업데이트:

`sass --watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력파일.scss|입력파일.sass</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력파일.css</span>
