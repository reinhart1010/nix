---
layout: page
title: common/xmlto (한국어)
description: "XML 문서에 XSL 스타일시트를 적용."
content_hash: b7b1c6e724ac8fd1372fe0741894a4bc2cb8e6fb
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/xmlto.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xmlto.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xmlto

XML 문서에 XSL 스타일시트를 적용.
더 많은 정보: <https://pagure.io/xmlto>.

- DocBook XML 문서를 PDF 형식으로 변환:

`xmlto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문서.xml</span>

- DocBook XML 문서를 HTML 형식으로 변환하고 결과 파일을 별도의 디렉토리에 저장:

`xmlto -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/html_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문서.xml</span>

- DocBook XML 문서를 단일 HTML 파일로 변환:

`xmlto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html-nochunks</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문서.xml</span>

- DocBook XML 문서를 변환할 때 사용할 스타일시트 지정:

`xmlto -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스타일시트.xsl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_포맷</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문서.xml</span>
