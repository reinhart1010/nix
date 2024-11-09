---
layout: page
title: linux/mmdebstrap (한국어)
description: "Debian chroot 생성 도구."
content_hash: 29aff519a6568526af45a880b079d26f582c390f
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/mmdebstrap.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mmdebstrap.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mmdebstrap

Debian chroot 생성 도구.
`debootstrap`의 대안.
더 많은 정보: <https://gitlab.mister-muffin.de/josch/mmdebstrap/>.

- Debian Stable 디렉토리 chroot 생성:

`sudo mmdebstrap stable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/debian-root/</span>

- 미러를 사용하여 Debian Bookworm tarball chroot 생성:

`mmdebstrap bookworm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/debian-bookworm.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://mirror.example.org/debian</span>

- 추가 패키지를 포함하여 Debian Sid tarball chroot 생성:

`mmdebstrap sid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/debian-sid.tar</span>` --include=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pkg1,pkg2</span>
