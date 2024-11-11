---
layout: page
title: linux/sysctl (한국어)
description: "커널 런타임 변수를 나열하고 변경합니다."
content_hash: dbb71e45ccd33dee9be11ae0b58805f16f62891c
last_modified_at: 2024-11-11
related_topics:
  - title: Deutsch version
    url: /de/linux/sysctl.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/sysctl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/sysctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/sysctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sysctl

커널 런타임 변수를 나열하고 변경합니다.
더 많은 정보: <https://manned.org/sysctl.8>.

- 사용 가능한 모든 변수와 그 값을 표시:

`sysctl -a`

- 변경 가능한 커널 상태 변수를 설정:

`sysctl -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">섹션.조정가능</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 현재 열려 있는 파일 핸들러 수를 확인:

`sysctl fs.file-nr`

- 동시에 열 수 있는 파일의 제한을 확인:

`sysctl fs.file-max`

- `/etc/sysctl.conf` 파일의 변경 사항을 적용:

`sysctl -p`
