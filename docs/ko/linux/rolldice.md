---
layout: page
title: linux/rolldice (한국어)
description: "가상 주사위를 굴립니다."
content_hash: 6f8329bcae0044cfedfd7ea3aab9d021af639197
last_modified_at: 2024-10-26
related_topics:
  - title: English version
    url: /en/linux/rolldice.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/rolldice.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rolldice.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rolldice

가상 주사위를 굴립니다.
더 많은 정보: <https://manned.org/rolldice>.

- 20면체 주사위 하나 굴리기:

`rolldice d`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>

- 6면체 주사위 두 개를 굴리고 낮은 값 제외:

`rolldice `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>`d`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6</span>`s`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- 20면체 주사위 두 개를 굴리고 수정자 값 추가:

`rolldice `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>`d`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+5</span>

- 20면체 주사위를 두 번 굴리기:

`rolldice `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>`xd`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>
