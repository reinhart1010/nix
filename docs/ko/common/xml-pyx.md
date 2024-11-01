---
layout: page
title: common/xml-pyx (한국어)
description: "XML 문서를 PYX (ESIS - ISO 8879) 형식으로 변환."
content_hash: ec2cddf926c82bf57c9101b89b0c63d9f43a76d0
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/xml-pyx.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xml-pyx.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xml pyx

XML 문서를 PYX (ESIS - ISO 8879) 형식으로 변환.
더 많은 정보: <https://xmlstar.sourceforge.net/docs.php>.

- XML 문서를 PYX 형식으로 변환:

`xml pyx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.xml|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pyx</span>

- `stdin`에서 XML 문서를 받아 PYX 형식으로 변환:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.xml</span>` | xml pyx > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pyx</span>

- 도움말 표시:

`xml pyx --help`
