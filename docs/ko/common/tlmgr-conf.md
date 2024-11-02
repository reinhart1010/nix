---
layout: page
title: common/tlmgr-conf (한국어)
description: "TeX Live 구성 관리."
content_hash: 1f988b7ee505a335691a46241fd9de63a110dceb
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/tlmgr-conf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tlmgr conf

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
