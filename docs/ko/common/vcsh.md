---
layout: page
title: common/vcsh (한국어)
description: "Git 저장소를 사용하여 홈 디렉토리를 위한 버전 관리 시스템."
content_hash: 617810d0f55d5df83d1b34aa9e26ed0ffc9989ad
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/vcsh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vcsh

Git 저장소를 사용하여 홈 디렉토리를 위한 버전 관리 시스템.
같이 보기: `chezmoi`, `stow`, `tuckr`, `homeshick`.
더 많은 정보: <https://github.com/RichiH/vcsh>.

- (빈) 저장소 초기화:

`vcsh init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_이름</span>

- 저장소를 사용자 지정 디렉토리 이름으로 클론:

`vcsh clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git_url</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_이름</span>

- 관리되는 모든 저장소 나열:

`vcsh list`

- 관리되는 저장소에서 Git 명령 실행:

`vcsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git_명령어</span>

- 모든 관리되는 저장소를 원격으로 푸시/풀:

`vcsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">push|pull</span>

- 관리되는 저장소에 대한 사용자 지정 `.gitignore` 파일 작성:

`vcsh write-gitignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_이름</span>
