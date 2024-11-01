---
layout: page
title: common/xml-depyx (한국어)
description: "PYX (ESIS - ISO 8879) 문서를 XML 형식으로 변환."
content_hash: c049bf71cf8756a0ef58d297f68293c8ec53cbdb
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/xml-depyx.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xml-depyx.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xml depyx

PYX (ESIS - ISO 8879) 문서를 XML 형식으로 변환.
더 많은 정보: <https://xmlstar.sourceforge.net/docs.php>.

- PYX (ESIS - ISO 8879) 문서를 XML 형식으로 변환:

`xml depyx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pyx|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.xml</span>

- `stdin`에서 PYX 문서를 XML 형식으로 변환:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pyx</span>` | xml depyx > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.xml</span>

- 도움말 표시:

`xml depyx --help`
