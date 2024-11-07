---
layout: page
title: common/lpadmin (한국어)
description: "CUPS 프린터 및 클래스를 구성."
content_hash: d32062f4125c58f93b5f102c3a6233b61e67a868
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/lpadmin.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/lpadmin.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/lpadmin.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/lpadmin.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lpadmin

CUPS 프린터 및 클래스를 구성.
같이 보기: `lpoptions`.
더 많은 정보: <https://openprinting.github.io/cups/doc/man-lpadmin.html>.

- 기본 프린터 설정:

`lpadmin -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프린터</span>

- 특정 프린터 또는 클래스 삭제:

`lpadmin -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프린터|클래스</span>

- 프린터를 클래스에 추가:

`lpadmin -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프린터</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클래스</span>

- 프린터를 클래스에서 제거:

`lpadmin -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프린터</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클래스</span>
