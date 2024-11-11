---
layout: page
title: linux/slurmdbd (한국어)
description: "Slurm를 위한 데이터베이스에 대한 안전한 엔터프라이즈 인터페이스."
content_hash: 52b1800a55baad03434386adb68ac2dd69d093fa
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/slurmdbd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/slurmdbd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># slurmdbd

Slurm를 위한 데이터베이스에 대한 안전한 엔터프라이즈 인터페이스.
더 많은 정보: <https://slurm.schedmd.com/slurmdbd.html>.

- 데몬의 우선순위를 지정된 값(일반적으로 음수)으로 설정:

`slurmdbd -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- `slurmdbd`의 작업 디렉토리를 LogFile 경로 또는 `/var/tmp`로 변경:

`slurmdbd -s`

- 도움말 표시:

`slurmdbd -h`

- 버전 표시:

`slurmdbd -V`
