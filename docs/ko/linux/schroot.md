---
layout: page
title: linux/schroot (한국어)
description: "다른 루트 디렉터리로 명령을 실행하거나 대화형 셸을 시작합니다. `chroot`보다 더 커스터마이즈 가능합니다."
content_hash: d51430c41eb2316481f5c216b37a6375551cd509
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/schroot.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/schroot.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># schroot

다른 루트 디렉터리로 명령을 실행하거나 대화형 셸을 시작합니다. `chroot`보다 더 커스터마이즈 가능합니다.
더 많은 정보: <https://wiki.debian.org/Schroot>.

- 사용 가능한 chroot 목록 나열:

`schroot --list`

- 특정 chroot에서 명령 실행:

`schroot --chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chroot</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 특정 chroot에서 옵션과 함께 명령 실행:

`schroot --chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chroot</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령_옵션</span>

- 모든 사용 가능한 chroot에서 명령 실행:

`schroot --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 특정 사용자로 특정 chroot 내에서 대화형 셸 시작:

`schroot --chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chroot</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>

- 새 세션 시작 (고유한 세션 ID가 `stdout`에 반환됨):

`schroot --begin-session --chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chroot</span>

- 기존 세션에 연결:

`schroot --run-session --chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세션_ID</span>

- 기존 세션 종료:

`schroot --end-session --chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세션_ID</span>
