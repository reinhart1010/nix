---
layout: page
title: linux/toolbox-rmi (한국어)
description: "`toolbox` 이미지 제거."
content_hash: 987cc3864b12e776944527cbc3ae77312fefcdd9
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/toolbox-rmi.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/toolbox-rmi.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/toolbox-rmi.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># toolbox rmi

`toolbox` 이미지 제거.
같이 보기: `toolbox rm`.
더 많은 정보: <https://manned.org/toolbox-rmi.1>.

- 하나 이상의 `toolbox` 이미지 제거:

`toolbox rmi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름1 이미지_이름2 ...</span>

- 모든 `toolbox` 이미지 제거:

`toolbox rmi --all`

- 현재 컨테이너에서 사용 중인 `toolbox` 이미지를 강제로 제거 (컨테이너도 함께 제거됨):

`toolbox rmi --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름</span>
