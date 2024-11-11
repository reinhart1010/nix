---
layout: page
title: linux/stress (한국어)
description: "CPU, 메모리 및 IO를 스트레스 테스트하는 Linux 시스템 도구."
content_hash: d92ae0557206b9cc3868d5300952bb9f47f37819
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/stress.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/stress.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># stress

CPU, 메모리 및 IO를 스트레스 테스트하는 Linux 시스템 도구.
더 많은 정보: <https://manned.org/stress>.

- CPU 스트레스 테스트를 위해 4개의 워커 생성:

`stress -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- IO 스트레스 테스트를 위해 2개의 워커 생성하고 5초 후 타임아웃:

`stress -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- 메모리 스트레스 테스트를 위해 2개의 워커 생성 (각 워커는 256M 바이트 할당):

`stress -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --vm-bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">256M</span>

- write()/unlink()를 반복하는 2개의 워커 생성 (각 워커는 1G 바이트 씀):

`stress -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --hdd-bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1GB</span>
