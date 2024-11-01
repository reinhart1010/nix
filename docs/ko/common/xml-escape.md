---
layout: page
title: common/xml-escape (한국어)
description: "특수 XML 문자를 이스케이프합니다. 예: `<a1>` → `&lt;a1&gt;`."
content_hash: 7f705ae4d686f2756ec350b842b3ba1d4729acb7
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/xml-escape.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xml-escape.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xml escape

특수 XML 문자를 이스케이프합니다. 예: `<a1>` → `&lt;a1&gt;`.
더 많은 정보: <https://xmlstar.sourceforge.net/doc/xmlstarlet.pdf>.

- 문자열에서 특수 XML 문자 이스케이프:

`xml escape "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><a1></span>`"`

- `stdin`에서 특수 XML 문자 이스케이프:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><a1></span>`" | xml escape`

- 도움말 표시:

`xml escape --help`
