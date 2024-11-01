---
layout: page
title: common/xml-canonic (한국어)
description: "XML 문서를 정규화."
content_hash: f7daaf43b744affaeafe0ae31777f5e6a025deaa
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/xml-canonic.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xml-canonic.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xml canonic

XML 문서를 정규화.
더 많은 정보: <https://xmlstar.sourceforge.net/docs.php>.

- XML 문서를 정규화하여 주석을 보존:

`xml canonic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.xml|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.xml</span>

- XML 문서를 정규화하여 주석 제거:

`xml canonic --without-comments `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.xml|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.xml</span>

- 파일의 XPATH를 사용하여 XML을 독점적으로 정규화하고, 주석을 보존:

`xml canonic --exc-with-comments `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.xml|URI</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/c14n.xpath</span>

- 도움말 표시:

`xml canonic --help`
