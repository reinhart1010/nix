---
layout: page
title: linux/flatpak-builder (한국어)
description: "애플리케이션의 의존성 빌드를 지원합니다."
content_hash: c2480a33ab2df302bd4573414a27dc695066b65d
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/linux/flatpak-builder.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/flatpak-builder.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># flatpak-builder

애플리케이션의 의존성 빌드를 지원합니다.
더 많은 정보: <https://docs.flatpak.org/en/latest/flatpak-builder-command-reference.html>.

- Flatpak을 빌드하고 새 저장소에 내보내기:

`flatpak-builder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/빌드_디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/매니페스트</span>

- Flatpak을 빌드하고 지정된 저장소에 내보내기:

`flatpak-builder --repo=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/빌드_디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/매니페스트</span>

- Flatpak을 빌드하고 로컬에 설치:

`flatpak-builder --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/빌드_디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/매니페스트</span>

- Flatpak을 빌드하고 서명하여 지정된 저장소에 내보내기:

`flatpak-builder --gpg-sign=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_아이디</span>` --repo=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/매니페스트</span>

- 애플리케이션 샌드박스 내부에서 설치 없이 셸 실행:

`flatpak-builder --run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/빌드_디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/매니페스트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh</span>
