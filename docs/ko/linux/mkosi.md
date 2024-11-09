---
layout: page
title: linux/mkosi (한국어)
description: "모던하고 레거시가 없는 리눅스 이미지를 빌드합니다."
content_hash: 9a9bbac02b42df8739e15301c95bb00b597a312d
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/mkosi.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mkosi.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mkosi

모던하고 레거시가 없는 리눅스 이미지를 빌드합니다.
`systemd`의 일부입니다.
더 많은 정보: <https://manned.org/mkosi>.

- 현재 빌드 구성을 표시하여 빌드될 내용을 확인:

`mkosi summary`

- 기본 설정으로 이미지 빌드 (배포판이 선택되지 않은 경우 호스트 시스템의 배포판 사용):

`mkosi build --distribution `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fedora|debian|ubuntu|arch|opensuse|...</span>

- 이미지를 빌드하고 해당 이미지의 systemd-nspawn 컨테이너에서 대화형 셸 실행:

`mkosi shell`

- QEMU를 사용하여 가상 머신에서 이미지 부팅 (디스크 이미지 또는 커널이 제공된 CPIO 이미지에 대해서만 지원):

`mkosi qemu`

- 도움말 표시:

`mkosi help`
