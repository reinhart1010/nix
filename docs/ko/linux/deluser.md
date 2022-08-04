---
layout: page
title: linux/deluser (한국어)
description: "유저 계정 제거 또는 그룹으로부터 사용자 제거."
content_hash: b6ee3a3f47788133172a44b724d8f5c82942b24f
related_topics:
  - title: English version
    url: /en/linux/deluser.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/deluser.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/deluser.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># deluser

유저 계정 제거 또는 그룹으로부터 사용자 제거.
더 많은 정보: <https://manpages.debian.org/latest/adduser/deluser.html>.

- 유저 삭제:

`deluser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 사용자의 홈 디렉토리 및 메일 스풀과 함께 사용자 제거:

`deluser -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 그룹으로부터 사용자 제거:

`deluser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹</span>
