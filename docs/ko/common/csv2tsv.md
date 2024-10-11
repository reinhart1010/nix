---
layout: page
title: common/csv2tsv (한국어)
description: "CSV (쉼표로 구분) 텍스트를 TSV (탭으로 구분) 형식으로 변환함."
content_hash: 7aa5a4111b4371bac773de05a9e6854380f71e11
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/csv2tsv.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/csv2tsv.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># csv2tsv

CSV (쉼표로 구분) 텍스트를 TSV (탭으로 구분) 형식으로 변환함.
더 많은 정보: <https://github.com/eBay/tsv-utils/blob/master/README.md#csv2tsv>.

- CSV를 TSV로 변환:

`csv2tsv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_csv1 경로/대상/입력_csv2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_csv</span>

- 필드 구분 기호로 구분되어 있는 CSV를 TSV로 변환:

`csv2tsv -c'`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">field_delimiter</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_csv</span>

- 세미콜론으로 구분된 CSV를 TSV로 변환:

`csv2tsv -c';' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_csv</span>
