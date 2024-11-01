---
layout: page
title: common/sshd (한국어)
description: "Secure Shell 데몬 - 원격 머신이 현재 머신에 안전하게 로그인할 수 있도록 허용합니다."
content_hash: 056254fc86d9547ffd7fd825458f188392650b5d
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/sshd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/sshd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sshd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sshd

Secure Shell 데몬 - 원격 머신이 현재 머신에 안전하게 로그인할 수 있도록 허용합니다.
원격 머신은 이 머신에서 실행되는 것처럼 명령을 실행할 수 있습니다.
더 많은 정보: <https://man.openbsd.org/sshd>.

- 백그라운드에서 데몬 시작:

`sshd`

- 포그라운드에서 sshd 실행:

`sshd -D`

- 자세한 출력으로 실행 (디버깅 용도):

`sshd -D -d`

- 특정 포트에서 실행:

`sshd -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>
