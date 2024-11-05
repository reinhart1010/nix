---
layout: page
title: common/x_x (한국어)
description: "Excel 및 CSV 파일 보기."
content_hash: 94208658aae5700a6d1d531cf1ddd0474d9a6b60
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/x_x.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/x_x.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># x_x

Excel 및 CSV 파일 보기.
더 많은 정보: <https://github.com/kristianperkins/x_x>.

- XLSX 또는 CSV 파일 보기:

`x_x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.xlsx|파일.csv</span>

- 첫 번째 행을 테이블 헤더로 사용하여 XLSX 또는 CSV 파일 보기:

`x_x -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.xlsx|파일.csv</span>

- 비전형적인 구분 기호를 사용하는 CSV 파일 보기:

`x_x --delimiter=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">';'</span>` --quotechar=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'|'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.csv</span>
