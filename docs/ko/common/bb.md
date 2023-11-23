---
layout: page
title: common/bb (한국어)
description: "스크립팅을 위한 기본 Clojure 인터프리터."
content_hash: 113a5579e627e2322d0d47619924fbf4f9a15eee
last_modified_at: 2023-11-23
related_topics:
  - title: English version
    url: /en/common/bb.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bb.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bb

스크립팅을 위한 기본 Clojure 인터프리터.
더 많은 정보: <https://book.babashka.org/#usage>.

- 표현식 평가:

`bb -e "(+ 1 2 3)"`

- 스크립트 파일 평가:

`bb -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.clj</span>

- `stdin`의 일련의 라인에 입력을 바인딩:

`printf "first\nsecond" | bb -i "(map clojure.string/capitalize *input*)"`

- `stdin`의 EDN(확장 가능한 데이터 표기법) 값 시퀀스에 입력을 바인딩:

`echo "{:key 'val}" | bb -I "(:key (first *input*))"`
