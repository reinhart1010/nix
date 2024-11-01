---
layout: page
title: common/xml-transform (한국어)
description: "XSLT를 사용하여 XML 문서를 변환."
content_hash: 41feae9db06fa1cbb22c36752e820ec61e71fb79
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/xml-transform.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xml-transform.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xml transform

XSLT를 사용하여 XML 문서를 변환.
더 많은 정보: <https://xmlstar.sourceforge.net/docs.php>.

- XSL 스타일시트를 사용하여 XML 문서를 변환하고, 하나의 XPATH 매개변수와 하나의 리터럴 문자열 매개변수를 전달:

`xml transform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스타일시트.xsl</span>` -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Count='count(/xml/table/rec)'</span>`" -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text="Count="</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.xml|URI</span>

- 도움말 표시:

`xml transform --help`
