---
layout: page
title: common/xkcdpass (한국어)
description: "강력한 암호를 생성하는 유연하고 스크립트 가능한 암호 생성기."
content_hash: f8db3a546b972726a1e9bcf4855ba3ecb16a695f
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/xkcdpass.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/xkcdpass.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xkcdpass.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xkcdpass

강력한 암호를 생성하는 유연하고 스크립트 가능한 암호 생성기.
XKCD 936에서 영감을 받았습니다.
더 많은 정보: <https://github.com/redacted/XKCD-password-generator>.

- 기본 옵션으로 하나의 암호 구문 생성:

`xkcdpass`

- 각 단어의 첫 글자가 제공된 인자와 일치하는 암호 구문 생성:

`xkcdpass -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">두운</span>

- 대화형으로 암호 생성:

`xkcdpass -i`
