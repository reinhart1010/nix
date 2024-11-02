---
layout: page
title: common/qemu (한국어)
description: "범용 머신 에뮬레이터 및 가상화 도구."
content_hash: 2a73f96cab0fa51d924f07e9910942f8cdb8b8b9
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/qemu.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/qemu.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qemu

범용 머신 에뮬레이터 및 가상화 도구.
다양한 CPU 아키텍처를 지원.
더 많은 정보: <https://www.qemu.org>.

- i386 아키텍처를 에뮬레이트하여 이미지에서 부팅:

`qemu-system-i386 -hda `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름.img</span>

- x64 아키텍처를 에뮬레이트하여 이미지에서 부팅:

`qemu-system-x86_64 -hda `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름.img</span>

- 라이브 ISO 이미지를 사용하여 QEMU 인스턴스 부팅:

`qemu-system-i386 -hda `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름.img</span>` -cdrom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">os_이미지.iso</span>` -boot d`

- 인스턴스에 할당할 RAM의 양 지정:

`qemu-system-i386 -m 256 -hda `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름.img</span>` -cdrom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">os_이미지.iso</span>` -boot d`

- 물리적 장치에서 부팅 (예: 부팅 가능한 매체 테스트를 위한 USB):

`qemu-system-i386 -hda `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/저장장치</span>
