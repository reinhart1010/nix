---
layout: page
title: common/emacs (한국어)
description: "확장 가능, 사용자 정의 가능, 자체 문서화가 되는 실시간 디스플레이 편집기."
content_hash: fd4e850c68883390c29b588a6be4ba827aac4260
last_modified_at: 2024-10-16
related_topics:
  - title: Deutsch version
    url: /de/common/emacs.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/emacs.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/emacs.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/emacs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/emacs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># emacs

확장 가능, 사용자 정의 가능, 자체 문서화가 되는 실시간 디스플레이 편집기.
참고: `emacsclient`.
더 많은 정보: <https://www.gnu.org/software/emacs>.

- Emacs 시작 및 파일 열기:

`emacs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 지정된 줄 번호에서 파일 열기:

`emacs +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">줄_번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- Emacs Lisp 파일을 스크립트로 실행:

`emacs --script `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.el</span>

- 콘솔 모드에서 Emacs를 시작 (X 윈도우 없이):

`emacs --no-window-system`

- 백그라운드에서 Emacs 서버를 시작 (`emacsclient`를 통해 액세스 가능):

`emacs --daemon`

- 실행 중인 Emacs 서버와 모든 인스턴스를 중지하고, 저장되지 않은 파일에 대한 확인을 요청:

`emacsclient --eval '(save-buffers-kill-emacs)'`

- Emacs에 파일을 저장:

`<Ctrl> + X, <Ctrl> + S`

- Emacs를 종료:

`<Ctrl> + X, <Ctrl> + C`
