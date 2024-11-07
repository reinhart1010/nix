---
layout: page
title: common/makepasswd (한국어)
description: "비밀번호 생성 및 암호화."
content_hash: 74d34af49130b7d0b598c52d8df677c572f30aa3
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/makepasswd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/makepasswd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># makepasswd

비밀번호 생성 및 암호화.
더 많은 정보: <https://manpages.debian.org/latest/makepasswd/makepasswd.1.en.html>.

- 무작위 비밀번호 생성 (8~10자, 문자 및 숫자 포함):

`makepasswd`

- 10자 길이의 비밀번호 생성:

`makepasswd --chars `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- 5~10자 길이의 비밀번호 생성:

`makepasswd --minchars `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` --maxchars `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- "b", "a", "r" 문자만 포함하는 비밀번호 생성:

`makepasswd --string `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>
