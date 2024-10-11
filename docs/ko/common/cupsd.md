---
layout: page
title: common/cupsd (한국어)
description: "CUPS 인쇄 서버용 서버 데몬."
content_hash: 4b20f69370aebd00ceea8862ec6dce3121da27c3
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/cupsd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/cupsd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cupsd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cupsd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cupsd

CUPS 인쇄 서버용 서버 데몬.
더 많은 정보: <https://openprinting.github.io/cups/doc/man-cupsd.html>.

- 백그라운드에서 `cupsd`를 데몬으로 시작:

`cupsd`

- 포어그라운드에서 `cupsd`를 시작:

`cupsd -f`

- 필요에 따라 `cupsd` 실행([l]aunch) (일반적으로 `launchd` 또는 `systemd`에서 사용됨):

`cupsd -l`

- Start `cupsd` using the specified [`c`]`upsd.conf` configuration file:

`cupsd -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/cupsd.conf</span>

- 지정된 `cups-file`[`s`]`.conf` 구성 파일을 사용하여 `cupsd`를 시작:

`cupsd -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/cups-파일.conf</span>

- [`c`]`upsd.conf` 구성 파일에 오류가 있는지 확인([t]est):

`cupsd -t -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/cupsd.conf</span>

- `cups-file`[`s`]`.conf` 구성 파일들에 오류가 있는지 확인([t]est):

`cupsd -t -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/cups-파일.conf</span>

- 도움말 표시:

`cupsd -h`
