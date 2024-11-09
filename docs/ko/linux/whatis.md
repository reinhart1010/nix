---
layout: page
title: linux/whatis (한국어)
description: "매뉴얼 페이지에서 한 줄 설명을 표시합니다."
content_hash: 19e6011de5bbf73388bb965211749436740927bf
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/whatis.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/whatis.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/linux/whatis.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/whatis.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># whatis

매뉴얼 페이지에서 한 줄 설명을 표시합니다.
더 많은 정보: <https://manned.org/whatis>.

- 매뉴얼 페이지에서 설명을 표시:

`whatis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 설명을 줄 끝에서 잘리지 않게 표시:

`whatis --long `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 와일드카드와 일치하는 모든 명령어에 대한 설명 표시:

`whatis --wildcard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">net*</span>

- 정규 표현식을 사용하여 매뉴얼 페이지 설명 검색:

`whatis --regex '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wish[0-9]\.[0-9]</span>`'`

- 특정 언어로 설명 표시:

`whatis --locale=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>
