---
layout: page
title: linux/aurvote (한국어)
description: "Arch User Repository의 패키지에 투표합니다."
content_hash: ffa5e3f6491f40b0e184ef4587a14e8d9341036f
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/aurvote.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aurvote.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/aurvote.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aurvote

Arch User Repository의 패키지에 투표합니다.
투표를 하려면 `~/.config/aurvote` 파일이 존재하고 AUR 자격 증명이 포함되어 있어야 합니다.
더 많은 정보: <https://github.com/archlinuxfr/aurvote>.

- 대화형으로 AUR 사용자명과 비밀번호를 포함한 `~/.config/aurvote` 파일 생성:

`aurvote --configure`

- 하나 이상의 AUR 패키지에 투표:

`aurvote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1 패키지2 ...</span>

- 하나 이상의 AUR 패키지에서 투표 취소:

`aurvote --unvote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1 패키지2 ...</span>

- 하나 이상의 AUR 패키지가 이미 투표되었는지 확인:

`aurvote --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1 패키지2 ...</span>

- 도움말 표시:

`aurvote --help`
