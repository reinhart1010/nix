---
layout: page
title: linux/modprobe (한국어)
description: "Linux 커널에 모듈을 추가하거나 제거합니다."
content_hash: dbb2ab088c3b9c35d46ca74426419b58e366146f
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/modprobe.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/modprobe.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/modprobe.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># modprobe

Linux 커널에 모듈을 추가하거나 제거합니다.
더 많은 정보: <https://manned.org/modprobe>.

- 모듈을 커널에 로드하는 것처럼 시뮬레이션하지만 실제로는 하지 않음:

`sudo modprobe --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>

- 모듈을 커널에 로드:

`sudo modprobe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>

- 모듈을 커널에서 제거:

`sudo modprobe --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>

- 모듈과 해당 모듈에 의존하는 모듈을 커널에서 제거:

`sudo modprobe --remove-dependencies `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>

- 커널 모듈의 의존성 표시:

`sudo modprobe --show-depends `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>
