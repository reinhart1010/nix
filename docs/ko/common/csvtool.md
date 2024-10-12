---
layout: page
title: common/csvtool (한국어)
description: "CSV 형식의 소스."
content_hash: 9b7f70ee59d304ec341940fbfbad94e853b99335
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/csvtool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# csvtool

CSV 형식의 소스.
더 많은 정보: <https://github.com/maroofi/csvtool>.

- CSV 파일에서 두 번째 열을 추출:

`csvtool --column `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.csv</span>

- CSV 파일에서 두 번째 및 네 번째 열을 추출:

`csvtool --column `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2,4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.csv</span>

- 두 번째 열이 'Foo'와 정확히 일치하는 CSV 파일에서 줄을 추출:

`csvtool --column `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --search '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">^Foo$</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.csv</span>

- 두 번째 열이 'Bar'로 시작하는 CSV 파일에서 줄을 추출:

`csvtool --column `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --search '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">^Bar</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.csv</span>

- 두 번째 열이 'Baz'로 끝나는 CSV 파일의 줄을 찾은 다음, 세 번째와 여섯 번째 열을 추출:

`csvtool --column `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --search '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Baz$</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.csv</span>` | csvtool --no-header --column `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3,6</span>
