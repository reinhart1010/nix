---
layout: page
title: linux/systemd-dissect (한국어)
description: "파일 시스템 OS 디스크 이미지, 특히 Discoverable Disk Images (DDIs)를 검사하고 상호작용."
content_hash: b9c94aefcefdeafb26b1641093526924c6bd5f81
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/linux/systemd-dissect.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/systemd-dissect.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># systemd-dissect

파일 시스템 OS 디스크 이미지, 특히 Discoverable Disk Images (DDIs)를 검사하고 상호작용.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemd-dissect.html>.

- OS 이미지에 대한 일반 정보 표시:

`systemd-dissect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/image.raw</span>

- OS 이미지 마운트:

`systemd-dissect --mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/image.raw</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/mnt/image</span>

- OS 이미지 언마운트:

`systemd-dissect --umount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/mnt/image</span>

- 이미지 내 파일 목록 나열:

`systemd-dissect --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/image.raw</span>

- OS 이미지를 자동으로 할당된 루프백 블록 장치에 연결하고 경로 출력:

`systemd-dissect --attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/image.raw</span>

- 루프백 블록 장치에서 OS 이미지 분리:

`systemd-dissect --detach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/장치</span>
