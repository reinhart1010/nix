---
layout: page
title: linux/fakeroot (한국어)
description: "파일 조작을 위해 루트 권한을 가장하는 환경에서 명령을 실행."
content_hash: e9a323bc10ca1c6b7c021a2b7e5ff75ed1031056
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/fakeroot.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/fakeroot.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fakeroot

파일 조작을 위해 루트 권한을 가장하는 환경에서 명령을 실행.
더 많은 정보: <https://manned.org/fakeroot.1>.

- fakeroot로 기본 셸 시작:

`fakeroot`

- fakeroot로 명령 실행:

`fakeroot -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령_인자들</span>

- fakeroot로 명령을 실행하고 종료 시 환경을 파일에 저장:

`fakeroot -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령_인자들</span>

- fakeroot 환경을 불러와 명령을 실행:

`fakeroot -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령_인자들</span>

- 파일의 실제 소유권을 유지하면서 명령 실행 (루트 소유로 가장하지 않음):

`fakeroot --unknown-is-real -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령_인자들</span>

- 도움말 표시:

`fakeroot --help`
