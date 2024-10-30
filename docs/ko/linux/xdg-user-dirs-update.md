---
layout: page
title: linux/xdg-user-dirs-update (한국어)
description: "XDG 사용자 디렉터리 업데이트."
content_hash: 720823c89f2cf7c7ca31ce2969f6efd203286247
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/linux/xdg-user-dirs-update.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xdg-user-dirs-update

XDG 사용자 디렉터리 업데이트.
더 많은 정보: <https://manned.org/xdg-user-dirs-update>.

- XDG의 DESKTOP 디렉터리를 지정한 디렉터리로 변경 (절대 경로여야 함):

`xdg-user-dirs-update --set DESKTOP "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>`"`

- 결과를 `user-dirs.dirs` 파일 대신 지정한 실행 파일에 기록:

`xdg-user-dirs-update --dummy-output "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/실행_파일</span>`" --set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xdg_사용자_디렉터리</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>`"`
