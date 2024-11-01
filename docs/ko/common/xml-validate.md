---
layout: page
title: common/xml-validate (한국어)
description: "XML 문서 유효성 검사."
content_hash: ece425778c6aadbac7058e3705630fd7a9e05c24
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/xml-validate.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xml-validate.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xml validate

XML 문서 유효성 검사.
더 많은 정보: <https://xmlstar.sourceforge.net/docs.php>.

- 하나 이상의 XML 문서가 잘 형성되었는지 검사:

`xml validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력1.xml|URI</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input2.xml ...</span>

- 하나 이상의 XML 문서를 문서 유형 정의(DTD)와 비교하여 유효성 검사:

`xml validate --dtd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스키마.dtd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력1.xml|URI</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input2.xml ...</span>

- 하나 이상의 XML 문서를 XML 스키마 정의(XSD)와 비교하여 유효성 검사:

`xml validate --xsd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스키마.xsd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력1.xml|URI</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input2.xml ...</span>

- 하나 이상의 XML 문서를 Relax NG 스키마(RNG)와 비교하여 유효성 검사:

`xml validate --relaxng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스키마.rng</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력1.xml|URI</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input2.xml ...</span>

- 도움말 표시:

`xml validate --help`
