---
layout: page
title: common/stow (한국어)
description: "심볼릭 링크 관리자."
content_hash: e459cfc028bf853152fe7376769a7986a42db55a
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/stow.html
    icon: bi bi-globe
tldri18n_status: 2
---
# stow

심볼릭 링크 관리자.
주로 dotfiles 관리를 위해 사용됩니다.
같이 보기: `chezmoi`, `tuckr`, `vcsh`, `homeshick`.
더 많은 정보: <https://www.gnu.org/software/stow>.

- 모든 파일을 주어진 디렉토리에 재귀적으로 심볼릭 링크 생성:

`stow --target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1 디렉토리1 파일2 디렉토리2</span>

- 주어진 디렉토리에서 심볼릭 링크를 재귀적으로 삭제:

`stow --delete --target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1 디렉토리1 파일2 디렉토리2</span>

- 결과가 어떻게 될지 시뮬레이션:

`stow --simulate --target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1 디렉토리1 파일2 디렉토리2</span>

- 삭제 후 다시 심볼릭 링크 생성:

`stow --restow --target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1 디렉토리1 파일2 디렉토리2</span>

- 정규 표현식과 일치하는 파일 제외:

`stow --ignore=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>` --target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1 디렉토리1 파일2 디렉토리2</span>
