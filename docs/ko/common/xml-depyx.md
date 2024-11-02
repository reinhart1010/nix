---
layout: page
title: common/xml-depyx (한국어)
description: "PYX (ESIS - ISO 8879) 문서를 XML 형식으로 변환."
content_hash: c049bf71cf8756a0ef58d297f68293c8ec53cbdb
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/xml-depyx.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xml depyx

PYX (ESIS - ISO 8879) 문서를 XML 형식으로 변환.
더 많은 정보: <https://xmlstar.sourceforge.net/docs.php>.

- PYX (ESIS - ISO 8879) 문서를 XML 형식으로 변환:

`xml depyx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pyx|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.xml</span>

- `stdin`에서 PYX 문서를 XML 형식으로 변환:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pyx</span>` | xml depyx > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.xml</span>

- 도움말 표시:

`xml depyx --help`
