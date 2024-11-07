---
layout: page
title: common/rector (한국어)
description: "PHP 5.3+ 코드를 업데이트하고 리팩토링하는 자동화 도구."
content_hash: 580e17692dfab7664edbfe63f643190c1dcf4e19
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/rector.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rector.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rector

PHP 5.3+ 코드를 업데이트하고 리팩토링하는 자동화 도구.
더 많은 정보: <https://github.com/rectorphp/rector>.

- 특정 디렉토리 처리:

`rector process `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 변경 사항을 적용하지 않고 디렉토리 처리 (드라이 런):

`rector process `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --dry-run`

- 디렉토리를 처리하고 코딩 표준 적용:

`rector process `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --with-style`

- 사용 가능한 레벨 목록 표시:

`rector levels`

- 특정 레벨로 디렉토리 처리:

`rector process `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레벨_이름</span>
