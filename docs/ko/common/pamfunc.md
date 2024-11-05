---
layout: page
title: common/pamfunc (한국어)
description: "Netpbm 이미지에 간단한 산술 함수를 적용."
content_hash: 79cc46914ac617a1f6bc0860f1ba5959deb3f7ac
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/pamfunc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamfunc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamfunc

Netpbm 이미지에 간단한 산술 함수를 적용.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pamfunc.html>.

- 지정된 PAM 이미지의 각 샘플에 `n`을 두 번째 인수로 하여 지정된 산술 함수 적용:

`pamfunc -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">multiplier|divisor|adder|subtractor|min|max</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>

- 지정된 PAM 이미지의 각 샘플에 `n`을 두 번째 인수로 하여 지정된 비트 문자열 함수 적용:

`pamfunc -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">andmask|ormask|xormask|shiftleft|shiftright</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>
