---
layout: page
title: linux/rpmspec (한국어)
description: "RPM 스펙 파일을 쿼리합니다."
content_hash: 4a16dc8e0ff656489cf95087cb44ccfe58c22f5b
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/rpmspec.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rpmspec.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rpmspec

RPM 스펙 파일을 쿼리합니다.
더 많은 정보: <https://manned.org/rpmspec>.

- RPM 스펙 파일에서 생성될 바이너리 패키지 나열:

`rpmspec --query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/rpm.spec</span>

- `--queryformat`의 모든 옵션 나열:

`rpmspec --querytags`

- RPM 스펙 파일에서 생성된 단일 바이너리 패키지의 요약 정보 가져오기:

`rpmspec --query --queryformat "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%{name}: %{summary}\n</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/rpm.spec</span>

- RPM 스펙 파일에서 생성될 소스 패키지 가져오기:

`rpmspec --query --srpm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/rpm.spec</span>

- RPM 스펙 파일을 `stdout`으로 파싱:

`rpmspec --parse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/rpm.spec</span>
