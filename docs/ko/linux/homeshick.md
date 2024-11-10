---
layout: page
title: linux/homeshick (한국어)
description: "Git dotfiles를 동기화합니다."
content_hash: 1c3d2a6d08326a2327192bf5726c66803b4e1132
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/homeshick.html
    icon: bi bi-globe
tldri18n_status: 2
---
# homeshick

Git dotfiles를 동기화합니다.
같이 보기: `chezmoi`, `stow`, `tuckr`, `vcsh`.
더 많은 정보: <https://github.com/andsens/homeshick/wiki>.

- 새로운 성(castle) 생성:

`homeshick generate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">성_이름</span>

- 성에 파일 추가:

`homeshick track `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">성_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 성으로 이동:

`homeshick cd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">성_이름</span>

- 성 복제:

`homeshick clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GitHub_사용자명</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_이름</span>

- 성의 모든 파일을 심볼릭 링크로 연결:

`homeshick link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">성_이름</span>
