---
layout: page
title: linux/etckeeper (한국어)
description: "시스템 구성 파일을 Git으로 추적합니다."
content_hash: ec1f717decf86fd7d31c8cc0a29963b4d77ce7d0
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/etckeeper.html
    icon: bi bi-globe
tldri18n_status: 2
---
# etckeeper

시스템 구성 파일을 Git으로 추적합니다.
더 많은 정보: <https://etckeeper.branchable.com/>.

- Git 저장소를 설정하고 다양한 설정 작업 수행(`/etc`에서 실행):

`sudo etckeeper init`

- `/etc`의 모든 변경 사항 커밋:

`sudo etckeeper commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>

- 임의의 Git 명령 실행:

`sudo etckeeper vcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">status</span>

- 커밋되지 않은 변경 사항이 있는지 확인(종료 코드만 반환):

`sudo etckeeper unclean`

- 기존 저장소를 삭제하고 변경 사항 추적 중지:

`sudo etckeeper uninit`
