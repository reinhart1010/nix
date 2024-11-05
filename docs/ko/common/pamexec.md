---
layout: page
title: common/pamexec (한국어)
description: "Netpbm 파일의 각 이미지에 대해 셸 명령을 실행."
content_hash: a000f2c046f59d5e593bdf61b594c622321f05b2
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/pamexec.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamexec.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamexec

Netpbm 파일의 각 이미지에 대해 셸 명령을 실행.
같이 보기: `pamfile`, `pampick`, `pamsplit`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pamexec.html>.

- Netpbm 파일의 각 이미지에 대해 셸 명령 실행:

`pamexec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pam</span>

- 명령이 비정상 종료 상태로 종료되면 처리를 중단:

`pamexec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pam</span>` -check`
