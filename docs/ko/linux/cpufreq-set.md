---
layout: page
title: linux/cpufreq-set (한국어)
description: "CPU 주파수 설정을 수정하는 도구."
content_hash: 16e1db92a38724e9ca91ce4b8e0941be35587273
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/cpufreq-set.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/cpufreq-set.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cpufreq-set

CPU 주파수 설정을 수정하는 도구.
주파수 값은 `cpufreq-info -l` 명령의 출력 범위 내에 있어야 합니다.
더 많은 정보: <https://manned.org/cpufreq-set>.

- CPU 1의 CPU 주파수 정책을 "userspace"로 설정:

`sudo cpufreq-set -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">userspace</span>

- CPU 1의 현재 최소 CPU 주파수 설정:

`sudo cpufreq-set -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --min `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">최소_주파수</span>

- CPU 1의 현재 최대 CPU 주파수 설정:

`sudo cpufreq-set -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --max `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">최대_주파수</span>

- CPU 1의 현재 작업 주파수 설정:

`sudo cpufreq-set -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_주파수</span>
