---
layout: page
title: linux/systemd-sysusers (한국어)
description: "시스템 사용자 및 그룹 생성."
content_hash: e69731d804d72775ff5bd6b4026a748e756f72f0
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/linux/systemd-sysusers.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/systemd-sysusers.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># systemd-sysusers

시스템 사용자 및 그룹 생성.
구성 파일이 지정되지 않으면 `sysusers.d` 디렉토리의 파일이 사용됩니다.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-sysusers.html>.

- 특정 구성 파일에서 사용자 및 그룹 생성:

`systemd-sysusers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 구성 파일을 처리하고 실제로 실행하지 않고 수행될 작업을 출력:

`systemd-sysusers --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 모든 구성 파일의 내용을 출력 (각 파일 앞에는 해당 파일 이름이 주석으로 출력됨):

`systemd-sysusers --cat-config`
