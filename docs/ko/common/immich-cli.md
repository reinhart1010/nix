---
layout: page
title: common/immich-cli (한국어)
description: "Immich에는 커멘드라인에서 특정 작업을 수행할 수 있는 커멘드라인 인터페이스 (CLI)가 있음."
content_hash: 670f2bd7103ca7d61ec2f6a0c74e2c31f90d1324
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/immich-cli.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/immich-cli.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/immich-cli.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># immich-cli

Immich에는 커멘드라인에서 특정 작업을 수행할 수 있는 커멘드라인 인터페이스 (CLI)가 있음.
참고: `immich-go`.
더 많은 정보: <https://immich.app/docs/features/command-line-interface/>.

- Immich 서버에 인증:

`immich login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_주소/api</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_키</span>

- 일부 이미지 파일 업로드:

`immich upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1.jpg 파일2.jpg</span>

- 하위 디렉터리를 포함한 디렉터리 업로드:

`immich upload --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 디렉터리를 기반으로 앨범 만들기:

`immich upload --album-name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">My summer holiday</span>`" --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- glob 패턴과 일치하는 리소스 건너뛰기:

`immich upload --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">**/Raw/** **/*.tif</span>` --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 숨겨진 파일 포함:

`immich upload --include-hidden --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>
