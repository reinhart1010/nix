---
layout: page
title: common/tlmgr-remove (한국어)
description: "TeX Live 패키지 제거."
content_hash: 8fe4d5c0cd1ac23b8e2e2c8a961b640930217695
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/tlmgr-remove.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tlmgr remove

TeX Live 패키지 제거.
기본적으로, 제거된 패키지는 TL 설치 디렉토리의 `./tlpkg/backups`에 백업됩니다.
더 많은 정보: <https://www.tug.org/texlive/tlmgr.html>.

- TeX Live 패키지 제거:

`sudo tlmgr remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지를 실제로 제거하지 않고 시뮬레이션:

`tlmgr remove --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지의 의존성을 제외하고 제거:

`sudo tlmgr remove --no-depends `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지를 특정 디렉토리에 백업하며 제거:

`sudo tlmgr remove --backupdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- TeX Live 전체를 제거하고 확인 요청:

`sudo tlmgr remove --all`
