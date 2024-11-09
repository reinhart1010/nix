---
layout: page
title: linux/udisksctl (한국어)
description: "`udisksd`와 상호 작용하여 스토리지 장치를 조회하고 조작."
content_hash: d088f2037fd83ca247e36e5bcd3ff26bc79aeb6f
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/udisksctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/udisksctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># udisksctl

`udisksd`와 상호 작용하여 스토리지 장치를 조회하고 조작.
더 많은 정보: <https://storaged.org/doc/udisks2-api/latest/udisksctl.1.html>.

- 디스크 드라이브 및 블록 장치에 대한 상위 정보 표시:

`udisksctl status`

- 장치에 대한 자세한 정보 표시:

`udisksctl info --block-device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- 장치 파티션에 대한 자세한 정보 표시:

`udisksctl info --block-device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- 장치 파티션을 마운트하고 마운트 지점을 출력:

`udisksctl mount --block-device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- 장치 파티션을 마운트 해제:

`udisksctl unmount --block-device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- 데몬의 이벤트 모니터링:

`udisksctl monitor`
