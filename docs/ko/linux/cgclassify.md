---
layout: page
title: linux/cgclassify (한국어)
description: "실행 중인 작업을 `cgroups`로 이동합니다."
content_hash: b05ea64fa16525abc862615313ea2628d83fbfcb
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/cgclassify.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/cgclassify.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/cgclassify.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/cgclassify.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cgclassify

실행 중인 작업을 `cgroups`로 이동합니다.
더 많은 정보: <https://manned.org/cgclassify>.

- 특정 PID를 가진 프로세스를 CPU 계층의 student 컨트롤 그룹으로 이동:

`cgclassify -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu:student</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>

- `/etc/cgrules.conf` 설정 파일에 기반하여 특정 PID를 가진 프로세스를 컨트롤 그룹으로 이동:

`cgclassify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>

- 특정 PID를 가진 프로세스를 CPU 계층의 student 컨트롤 그룹으로 이동(서비스 `cgred`의 데몬이 해당 PID 및 자식의 `cgroups`를 변경하지 않음, `/etc/cgrules.conf` 기반):

`cgclassify --sticky -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu:/student</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>
