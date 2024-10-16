---
layout: page
title: common/emacsclient (한국어)
description: "기존 Emacs 서버에서 파일을 열기."
content_hash: 754a80264bf72477f8ac404983ffdd6bf7b98332
last_modified_at: 2024-10-16
related_topics:
  - title: Deutsch version
    url: /de/common/emacsclient.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/emacsclient.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/emacsclient.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/emacsclient.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># emacsclient

기존 Emacs 서버에서 파일을 열기.
참고: `emacs`.
더 많은 정보: <https://www.gnu.org/software/emacs/manual/html_node/emacs/emacsclient-Options.html>.

- 기존 Emacs 서버에서 파일을 열기 (사용 가능한 경우, GUI 사용):

`emacsclient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 콘솔 모드에서 파일 열기 (X 윈도우 없이):

`emacsclient --no-window-system `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 새로운 Emacs 창에서 파일을 열기:

`emacsclient --create-frame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 명령을 평가하고 출력을 `stdout`으로 출력한 다음 종료:

`emacsclient --eval '(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>`)'`

- Emacs 서버가 실행되고 있지 않은 경우, 대체 편집기를 지정:

`emacsclient --alternate-editor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">에디터</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 실행 중인 Emacs 서버와 모든 인스턴스를 중지, 저장되지 않은 파일에 대한 확인을 요청:

`emacsclient --eval '(save-buffers-kill-emacs)'`
