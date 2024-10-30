---
layout: page
title: common/guile (한국어)
description: "Guile 스키마 해석기."
content_hash: b710eb905d4851252aa6503823afbfc198a58bc6
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/guile.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/guile.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># guile

Guile 스키마 해석기.
더 많은 정보: <https://www.gnu.org/software/guile>.

- REPL(대화형 쉘)을 시작:

`guile`

- 지정된 스키마 파일에서 스크립트를 실행:

`guile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스크립트.scm</span>

- 스키마 표현식 실행:

`guile -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">표현식</span>`"`

- 원격 REPL 연결을 위해 포트 또는 Unix 도메인 소켓(기본값은 37146포트):

`guile --listen=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트_또는_소켓</span>
