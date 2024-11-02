---
layout: page
title: common/tlmgr-update (한국어)
description: "TeX Live 패키지 업데이트."
content_hash: ed6cc04a19e5630583b4890eaca17e355aebf60c
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/tlmgr-update.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tlmgr update

TeX Live 패키지 업데이트.
더 많은 정보: <https://www.tug.org/texlive/tlmgr.html>.

- 모든 TeX Live 패키지를 업데이트:

`sudo tlmgr update --all`

- tlmgr 자체 업데이트:

`sudo tlmgr update --self`

- 특정 패키지 업데이트:

`sudo tlmgr update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 특정 패키지를 제외하고 모든 패키지 업데이트:

`sudo tlmgr update --all --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 현재 패키지의 백업을 만들며 모든 패키지 업데이트:

`sudo tlmgr update --all --backup`

- 의존성을 업데이트하지 않고 특정 패키지 업데이트:

`sudo tlmgr update --no-depends `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 아무런 변경 없이 모든 패키지 업데이트를 시뮬레이션:

`sudo tlmgr update --all --dry-run`
