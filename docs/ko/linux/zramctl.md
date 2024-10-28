---
layout: page
title: linux/zramctl (한국어)
description: "zram 장치를 설정하고 제어."
content_hash: 5a9efa82e70406292cadd126f27ce0be4bf665d3
last_modified_at: 2024-10-28
related_topics:
  - title: English version
    url: /en/linux/zramctl.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/zramctl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/zramctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/zramctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/zramctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zramctl

zram 장치를 설정하고 제어.
`mkfs` 또는 `mkswap`를 사용하여 zram 장치를 파티션으로 포맷하세요.
더 많은 정보: <https://manned.org/zramctl>.

- zram이 활성화되어 있는지 확인:

`lsmod | grep -i zram`

- 동적 장치 수로 zram 활성화 (`zramctl`을 사용하여 장치를 추가로 구성):

`sudo modprobe zram`

- 정확히 2개의 장치로 zram 활성화:

`sudo modprobe zram num_devices=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- 다음 사용 가능한 zram 장치를 찾아 LZ4 압축을 사용하여 2GB 가상 드라이브로 초기화:

`sudo zramctl --find --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2GB</span>` --algorithm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lz4</span>

- 현재 초기화된 장치 나열:

`sudo zramctl`
