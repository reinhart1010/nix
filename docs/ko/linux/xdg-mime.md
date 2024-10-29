---
layout: page
title: linux/xdg-mime (한국어)
description: "XDG 표준에 따라 MIME 유형을 조회하고 관리."
content_hash: 214ab2a64613221a46d1ecfc03a709ac7b7e6503
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/xdg-mime.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/xdg-mime.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xdg-mime

XDG 표준에 따라 MIME 유형을 조회하고 관리.
더 많은 정보: <https://portland.freedesktop.org/doc/xdg-mime.html>.

- 파일의 MIME 유형 표시:

`xdg-mime query filetype `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- PNG 파일을 여는 기본 애플리케이션 표시:

`xdg-mime query default `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image/png</span>

- 특정 파일을 여는 기본 애플리케이션 표시:

`xdg-mime query default $(xdg-mime query filetype `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>`)`

- PNG 및 JPEG 이미지를 여는 기본 애플리케이션을 imv로 설정:

`xdg-mime default `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imv.desktop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image/png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image/jpeg</span>
