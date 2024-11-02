---
layout: page
title: common/tlmgr-install (한국어)
description: "TeX Live 패키지 설치."
content_hash: 69dc6240ee08863569e1e237ea8ef9897d842eb6
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/tlmgr-install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tlmgr install

TeX Live 패키지 설치.
더 많은 정보: <https://www.tug.org/texlive/tlmgr.html>.

- 패키지 및 의존성 설치:

`sudo tlmgr install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 재설치:

`sudo tlmgr install --reinstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지를 설치하는 시뮬레이션을 실행하되 실제 변경은 하지 않음:

`tlmgr install --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지를 의존성 없이 설치:

`sudo tlmgr install --no-depends `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 특정 파일에서 패키지 설치:

`sudo tlmgr install --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패키지</span>
