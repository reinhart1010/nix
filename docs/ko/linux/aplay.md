---
layout: page
title: linux/aplay (한국어)
description: "ALSA 사운드카드 드라이버를 위한 사운드 플레이어."
content_hash: f5ac337ad2a7539485e80a73738a283fb8abe1e1
last_modified_at: 2024-11-08
related_topics:
  - title: Deutsch version
    url: /de/linux/aplay.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/aplay.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/aplay.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aplay.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/aplay.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aplay

ALSA 사운드카드 드라이버를 위한 사운드 플레이어.
더 많은 정보: <https://manned.org/aplay>.

- 특정 파일 재생 (파일 형식에 따라 샘플링 속도, 비트 깊이 등이 자동으로 결정됨):

`aplay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 파일의 처음 10초를 2500 Hz에서 재생:

`aplay --duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2500</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 22050 Hz, 모노, 8비트, Mu-Law `.au` 파일로 원시 파일 재생:

`aplay --channels=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --file-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raw</span>` --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22050</span>` --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mu_law</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
