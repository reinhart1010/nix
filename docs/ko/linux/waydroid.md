---
layout: page
title: linux/waydroid (한국어)
description: "Ubuntu와 같은 일반적인 Linux 시스템에서 전체 Android 시스템을 부팅하기 위한 컨테이너 기반 접근 방식."
content_hash: 3407d5ef9a0f82e95504be8470733b9df37d6d78
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/waydroid.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/waydroid.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># waydroid

Ubuntu와 같은 일반적인 Linux 시스템에서 전체 Android 시스템을 부팅하기 위한 컨테이너 기반 접근 방식.
더 많은 정보: <https://docs.waydro.id>.

- Waydroid 시작:

`waydroid`

- Waydroid 초기화 (최초 실행 시 또는 Android를 재설치한 후 필요):

`sudo waydroid init`

- 파일에서 새로운 Android 앱 설치:

`waydroid app install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.apk</span>

- 패키지 이름으로 Android 앱 실행:

`waydroid app launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>

- Waydroid 세션 시작 또는 중지:

`waydroid session `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>

- Waydroid 컨테이너 관리:

`sudo waydroid container `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|restart|freeze|unfreeze</span>

- Waydroid 셸 열기:

`sudo waydroid shell`

- Waydroid 창 크기 조정:

`waydroid prop set persist.waydroid.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width|height</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>
