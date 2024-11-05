---
layout: page
title: common/pamsplit (한국어)
description: "여러 이미지가 포함된 Netpbm 파일을 단일 이미지 Netpbm 파일로 분할."
content_hash: b5a229222b815ef7b1b67e15405cb40e58f1011d
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/pamsplit.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pamsplit.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamsplit.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamsplit

여러 이미지가 포함된 Netpbm 파일을 단일 이미지 Netpbm 파일로 분할.
같이 보기: `pamfile`, `pampick`, `pamexec`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pamsplit.html>.

- 여러 이미지가 포함된 Netpbm 파일을 단일 이미지 Netpbm 파일로 분할:

`pamsplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pam</span>

- 출력 파일의 이름 패턴 지정:

`pamsplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_%d.pam</span>
