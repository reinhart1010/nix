---
layout: page
title: common/z (한국어)
description: "사용 빈도가 높은 디렉토리를 추적하고, 문자열 패턴이나 정규 표현식을 사용하여 빠르게 이동할 수 있게 합니다."
content_hash: 82ce3b5f3a676d589fb177830207a863cb7caaea
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/z.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/z.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/z.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/z.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/z.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># z

사용 빈도가 높은 디렉토리를 추적하고, 문자열 패턴이나 정규 표현식을 사용하여 빠르게 이동할 수 있게 합니다.
더 많은 정보: <https://github.com/rupa/z>.

- 이름에 "foo"가 포함된 디렉토리로 이동:

`z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- 이름에 "foo"와 그 다음에 "bar"가 포함된 디렉토리로 이동:

`z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>

- "foo"와 일치하는 가장 높은 순위의 디렉토리로 이동:

`z -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- "foo"와 일치하는 가장 최근에 접근한 디렉토리로 이동:

`z -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- `z`의 데이터베이스에서 "foo"와 일치하는 모든 디렉토리 나열:

`z -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- 현재 디렉토리를 `z`의 데이터베이스에서 제거:

`z -x .`

- 현재 디렉토리의 하위 디렉토리로 일치 항목을 제한:

`z -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>
