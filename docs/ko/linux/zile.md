---
layout: page
title: linux/zile (한국어)
description: "Emacs 텍스트 편집기의 경량 클론."
content_hash: d1addd08f404890611b19a2d5fd77b84f24330e0
last_modified_at: 2024-10-28
related_topics:
  - title: English version
    url: /en/linux/zile.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/zile.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zile

Emacs 텍스트 편집기의 경량 클론.
더 많은 정보: <https://www.gnu.org/software/zile/>.

- 임시 메모를 위한 버퍼 시작 (저장되지 않음):

`zile`

- 파일 열기:

`zile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일 저장:

`<Ctrl> + X, <Ctrl> + S`

- 종료:

`<Ctrl> + X, <Ctrl> + C`

- 지정된 줄 번호에서 파일 열기:

`zile +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">줄_번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 변경 사항 실행 취소:

`<Ctrl> + X, U`
