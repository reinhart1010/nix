---
layout: page
title: common/lebab (한국어)
description: "ES6/ES7로 코드 변환을 위한 JavaScript 모더나이저."
content_hash: d7fcec6ac42e9b3b6e294d5d34ed218a476aecce
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/lebab.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/lebab.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lebab

ES6/ES7로 코드 변환을 위한 JavaScript 모더나이저.
모든 예시에 대한 변환이 제공되어야 합니다.
더 많은 정보: <https://github.com/lebab/lebab>.

- 하나 이상의 쉼표로 구분된 변환을 사용하여 트랜스파일:

`lebab --transform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변환1,변환2,...</span>

- 파일을 `stdout`으로 트랜스파일:

`lebab `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>

- 파일을 지정된 출력 파일로 트랜스파일:

`lebab `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` --out-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- 지정된 디렉토리, 글로브 또는 파일의 모든 `.js` 파일을 제자리에서 대체:

`lebab --replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉토리|글로브|파일</span>

- 도움말 표시:

`lebab --help`
