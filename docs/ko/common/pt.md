---
layout: page
title: common/pt (한국어)
description: "Platinum Searcher."
content_hash: 5aa4579616d849a9d53ebb2dc48910592ea929e1
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pt

Platinum Searcher.
`ag`와 유사한 코드 검색 도구.
더 많은 정보: <https://github.com/monochromegane/the_platinum_searcher>.

- "foo"를 포함하는 파일을 찾아 일치하는 부분을 강조하여 출력:

`pt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- "foo"를 포함하는 파일을 찾아 각 파일의 일치 개수 표시:

`pt -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- "foo"를 단어 전체로 취급하고 대소문자 무시하여 찾기:

`pt -wi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- 정규 표현식을 사용하여 특정 확장자를 가진 파일에서 "foo" 찾기:

`pt -G='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\.bar$</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- 최대 2단계 디렉토리 깊이까지 정규 표현식과 일치하는 파일 찾기:

`pt --depth=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">^ba[rz]*$</span>`'`
