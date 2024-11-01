---
layout: page
title: common/xmllint (한국어)
description: "XPath를 지원하는 XML 파서 및 린터로, XML 트리를 탐색할 수 있는 구문입니다."
content_hash: 18529d8d7484eb2bf6be20d2cdef4cd9986272f5
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/xmllint.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xmllint.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xmllint

XPath를 지원하는 XML 파서 및 린터로, XML 트리를 탐색할 수 있는 구문입니다.
더 많은 정보: <https://manned.org/xmllint>.

- 이름이 "foo"인 모든 노드(태그) 반환:

`xmllint --xpath "//`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_파일.xml</span>

- 이름이 "foo"인 첫 번째 노드의 내용을 문자열로 반환:

`xmllint --xpath "string(//`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>`)" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_파일.xml</span>

- HTML 파일에서 두 번째 앵커 요소의 href 속성 반환:

`xmllint --html --xpath "string(//a[2]/@href)" webpage.xhtml`

- 파일에서 사람이 읽을 수 있는(들여쓰기 된) XML 반환:

`xmllint --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_파일.xml</span>

- XML 파일이 DOCTYPE 선언의 요구 사항을 충족하는지 확인:

`xmllint --valid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_파일.xml</span>

- 온라인에 호스팅된 DTD 스키마에 대해 XML 유효성 검사:

`xmllint --dtdvalid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">URL</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_파일.xml</span>
