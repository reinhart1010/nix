---
layout: page
title: common/fakedata (한국어)
description: "다양한 생성기를 사용하여 가짜 데이터를 생성."
content_hash: ff6decab3c1979b0dc0fc64e09e506dc04648226
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/fakedata.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fakedata.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fakedata

다양한 생성기를 사용하여 가짜 데이터를 생성.
더 많은 정보: <https://github.com/lucapette/fakedata>.

- 유효한 모든 생성기를 나열:

`fakedata --generators`

- 하나 이상의 생성기를 사용하여 데이터를 생성:

`fakedata `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">생성기1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">생성기2</span>

- 특정 출력 형식으로 데이터를 생성:

`fakedata --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">csv|tab|sql</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">생성기</span>

- 주어진 수의 데이터 항목을 생성 (기본값은 10):

`fakedata --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">생성기</span>

- 사용자 정의 출력 템플릿을 사용하여 데이터를 생성 (생성기 이름의 첫 글자는 대문자여야 함):

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\{\{Generator\}\}</span>`" | fakedata`
