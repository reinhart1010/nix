---
layout: page
title: common/brittany (한국어)
description: "Haskell 소스 파일을 형식에 맞추어 출력."
content_hash: 9744cf0f1a173816dbc5c76dae53b76350cb4280
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/brittany.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/brittany.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># brittany

Haskell 소스 파일을 형식에 맞추어 출력.
더 많은 정보: <https://github.com/lspitzner/brittany#readme>.

- Haskell 소스 파일의 형식을 지정하고 결과를 `stdout`으로 인쇄:

`brittany `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/file.hs</span>

- 현재 디렉터리에 있는 모든 Haskell 소스 파일을 바로 포맷:

`brittany --write-mode=inplace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.hs</span>

- Haskell 소스 파일에 변경이 필요한지 확인하고 프로그램 종료 코드를 통해 결과를 표시:

`brittany --check-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/file.hs</span>

- 들여쓰기 수준, 줄 길이 별로 지정된 공백 설정을 사용하여 Haskell 소스 파일 형식을 지정:

`brittany --indent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` --columns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/file.hs</span>

- 지정된 구성 파일에 정의된 스타일에 따라 Haskell 소스 파일의 형식을 지정:

`brittany --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/config.yaml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/file.hs</span>
