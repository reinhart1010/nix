---
layout: page
title: common/alacritty (한국어)
description: "교차 플랫폼으로, GPU-가속 터미널 에뮬레이터."
content_hash: 59689ee3008f5d1331024ad3ffc8ef3b5629eadd
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/alacritty.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/alacritty.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/alacritty.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/alacritty.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/alacritty.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/alacritty.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/alacritty.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/alacritty.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/alacritty.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/alacritty.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># alacritty

교차 플랫폼으로, GPU-가속 터미널 에뮬레이터.
더 많은 정보: <https://github.com/alacritty/alacritty>.

- 새 Alacritty 창 열기:

`alacritty`

- 특정 디렉토리에서 실행:

`alacritty --working-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/디렉토리명</span>

- 새로운 Alacritty 창에서 명령어 실행:

`alacritty -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 대체 구성파일 지정 (기본값 : `$XDG_CONFIG_HOME/alacritty/alacritty.toml`):

`alacritty --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/config.toml</span>

- 재배치가 가능한 라이브 구성 설정으로 실행 (기본적으로 `alacritty.toml` 에서도 활성화 가능):

`alacritty --live-config-reload --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/config.toml</span>
