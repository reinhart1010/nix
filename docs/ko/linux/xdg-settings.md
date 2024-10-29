---
layout: page
title: linux/xdg-settings (한국어)
description: "XDG 호환 데스크탑 환경의 설정 관리."
content_hash: f025dccd29f6ae726e187c4a965a259c3c172e3b
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/xdg-settings.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/xdg-settings.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xdg-settings

XDG 호환 데스크탑 환경의 설정 관리.
더 많은 정보: <https://portland.freedesktop.org/doc/xdg-settings.html>.

- 기본 웹 브라우저 출력:

`xdg-settings get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기본-웹-브라우저</span>

- 기본 웹 브라우저를 Firefox로 설정:

`xdg-settings set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기본-웹-브라우저</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firefox.desktop</span>

- 기본 메일 URL 스킴 핸들러를 Evolution으로 설정:

`xdg-settings set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기본-url-스킴-핸들러</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mailto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">evolution.desktop</span>

- 기본 PDF 문서 뷰어 설정:

`xdg-settings set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf-뷰어.desktop</span>

- 도움말 표시:

`xdg-settings --help`
