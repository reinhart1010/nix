---
layout: page
title: common/tlmgr-conf (한국어)
description: "TeX Live 구성 관리."
content_hash: 1f988b7ee505a335691a46241fd9de63a110dceb
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/tlmgr-conf.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tlmgr-conf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tlmgr conf

TeX Live 구성 관리.
더 많은 정보: <https://www.tug.org/texlive/tlmgr.html>.

- 현재 TeX Live 구성 보기:

`tlmgr conf`

- 현재 `texmf`, `tlmgr`, 또는 `updmap` 구성 보기:

`tlmgr conf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texmf|tlmgr|updmap</span>

- 특정 구성 옵션만 보기:

`tlmgr conf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texmf|tlmgr|updmap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_키</span>

- 특정 구성 옵션 설정:

`tlmgr conf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texmf|tlmgr|updmap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_키</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 특정 구성 옵션 삭제:

`tlmgr conf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texmf|tlmgr|updmap</span>` --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_키</span>

- `\write18`을 통한 시스템 호출 실행 비활성화:

`tlmgr conf texmf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_escape</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>

- 모든 추가 `texmf` 트리 보기:

`tlmgr conf auxtrees show`
