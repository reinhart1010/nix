---
layout: page
title: linux/hyprpm (한국어)
description: "Hyprland Wayland 컴포지터의 플러그인을 제어."
content_hash: 29f834fa020855262a2010c9b0931c53bad4314b
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/hyprpm.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/hyprpm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/hyprpm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hyprpm

Hyprland Wayland 컴포지터의 플러그인을 제어.
더 많은 정보: <https://wiki.hyprland.org/Plugins/Using-Plugins/#hyprpm>.

- 플러그인 추가:

`hyprpm add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git_url</span>

- 플러그인 제거:

`hyprpm remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git_url|플러그인_이름</span>

- 플러그인 활성화:

`hyprpm enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플러그인_이름</span>

- 플러그인 비활성화:

`hyprpm disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플러그인_이름</span>

- 모든 플러그인 업데이트 및 확인:

`hyprpm update`

- 작업 강제 실행:

`hyprpm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--force</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업</span>

- 설치된 모든 플러그인 나열:

`hyprpm list`
