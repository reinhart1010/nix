---
layout: page
title: common/qr (한국어)
description: "ANSI VT-100 이스케이프 코드를 사용하여 터미널에서 QR 코드를 생성."
content_hash: fc41659284fac3f8b5213ca50a27d605e13a9d18
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/qr.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/qr.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qr

ANSI VT-100 이스케이프 코드를 사용하여 터미널에서 QR 코드를 생성.
더 많은 정보: <https://github.com/lincolnloop/python-qrcode/>.

- QR 코드 생성:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터</span>`" | qr`

- 오류 수정 수준 지정 (기본값은 M):

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터</span>`" | qr --error-correction=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">L|M|Q|H</span>
