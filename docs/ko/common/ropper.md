---
layout: page
title: common/ropper (한국어)
description: "바이너리 파일에서 ROP 가젯을 찾습니다."
content_hash: 8fb0980f8cf83e74a71433c95e3d191177c17354
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/ropper.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ropper.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ropper

바이너리 파일에서 ROP 가젯을 찾습니다.
더 많은 정보: <https://scoding.de/ropper/>.

- 바이너리 파일의 가젯 나열:

`ropper --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>

- 정규 표현식을 사용하여 바이너리 파일의 가젯 필터링:

`ropper --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>` --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>

- 지정된 유형의 가젯을 바이너리 파일에서 나열:

`ropper --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rop|job|sys|all</span>

- 바이너리 파일에서 불량 바이트 가젯 제외:

`ropper --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>` --badbytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">바이트_문자열</span>

- 지정된 명령어 수까지의 가젯을 바이너리 파일에서 나열:

`ropper --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>` --inst-count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">수량</span>
