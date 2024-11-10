---
layout: page
title: common/tabula (한국어)
description: "PDF 파일에서 테이블을 추출."
content_hash: 82c7084351995e8ed4f2ffa27e8c9b6720065ce1
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/tabula.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tabula

PDF 파일에서 테이블을 추출.
더 많은 정보: <https://tabula.technology>.

- PDF에서 모든 테이블을 CSV 파일로 추출:

`tabula -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.csv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.pdf</span>

- PDF에서 모든 테이블을 JSON 파일로 추출:

`tabula --format JSON -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.pdf</span>

- PDF의 1, 2, 3, 6 페이지에서 테이블 추출:

`tabula --pages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-3,6</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.pdf</span>

- PDF의 1 페이지에서 테이블을 추출하며, 분석할 페이지의 부분을 추측:

`tabula --guess --pages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.pdf</span>

- 셀 경계를 결정하기 위해 줄을 사용하여 PDF에서 모든 테이블 추출:

`tabula --spreadsheet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.pdf</span>

- 셀 경계를 결정하기 위해 빈 공간을 사용하여 PDF에서 모든 테이블 추출:

`tabula --no-spreadsheet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.pdf</span>
