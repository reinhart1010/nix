---
layout: page
title: linux/gnome-software (한국어)
description: "애플리케이션을 추가 및 제거하고 시스템을 업데이트합니다."
content_hash: 14d8c2e33836d2611ad04bff61103d96eeb8ae3d
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/gnome-software.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/gnome-software.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/gnome-software.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gnome-software

애플리케이션을 추가 및 제거하고 시스템을 업데이트합니다.
더 많은 정보: <https://apps.gnome.org/app/org.gnome.Software/>.

- GNOME Software GUI를 실행 중이 아니면 시작:

`gnome-software`

- GNOME Software GUI를 실행 중이 아니면 시작하고, 지정된 페이지로 이동:

`gnome-software --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">업데이트|업데이트됨|설치됨|개요</span>

- GNOME Software GUI를 실행 중이 아니면 시작하고, 지정된 패키지의 세부 정보를 보기:

`gnome-software --details `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 버전 표시:

`gnome-software --version`
