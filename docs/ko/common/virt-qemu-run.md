---
layout: page
title: common/virt-qemu-run (한국어)
description: "`libvirtd`와 독립적으로 QEMU 게스트 VM을 실행하기 위한 실험 도구."
content_hash: cf842ebe67a042119072cdd623dedf82705229a1
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/virt-qemu-run.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/virt-qemu-run.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/virt-qemu-run.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># virt-qemu-run

`libvirtd`와 독립적으로 QEMU 게스트 VM을 실행하기 위한 실험 도구.
더 많은 정보: <https://libvirt.org/manpages/virt-qemu-run.html>.

- QEMU 가상 머신 실행:

`virt-qemu-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/guest.xml</span>

- QEMU 가상 머신을 실행하고 상태를 특정 디렉토리에 저장:

`virt-qemu-run --root=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/guest.xml</span>

- QEMU 가상 머신을 실행하고 시작에 대한 자세한 정보 표시:

`virt-qemu-run --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/guest.xml</span>

- 도움말 표시:

`virt-qemu-run --help`
