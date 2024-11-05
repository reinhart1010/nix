---
layout: page
title: common/pampick (한국어)
description: "여러 이미지로 구성된 Netpbm 스트림에서 이미지를 선택."
content_hash: 4d1e6d5f04fcc60f18f94cdcef8307bd9efcc213
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/pampick.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pampick.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pampick

여러 이미지로 구성된 Netpbm 스트림에서 이미지를 선택.
같이 보기: `pamfile`, `pamsplit`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pampick.html>.

- Netpbm 파일의 각 이미지에서 셸 명령 실행:

`pampick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_번호1 이미지_번호2 ...</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>
