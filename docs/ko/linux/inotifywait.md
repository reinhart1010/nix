---
layout: page
title: linux/inotifywait (한국어)
description: "파일 변경을 대기합니다."
content_hash: 1b655c420515df0a5250c39837fb41838cbba342
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/inotifywait.html
    icon: bi bi-globe
tldri18n_status: 2
---
# inotifywait

파일 변경을 대기합니다.
더 많은 정보: <https://manned.org/inotifywait>.

- 특정 파일의 이벤트를 감시하고 첫 번째 이벤트 이후 종료:

`inotifywait `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 파일의 이벤트를 종료하지 않고 지속적으로 감시:

`inotifywait --monitor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 폴더의 이벤트를 재귀적으로 감시:

`inotifywait --monitor --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 정규 표현식과 일치하는 파일을 제외하고 폴더의 변경 사항 감시:

`inotifywait --monitor --recursive --exclude "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 30초 동안 이벤트가 발생하지 않으면 종료하며 파일의 변경 사항 감시:

`inotifywait --monitor --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일 수정 이벤트만 감시:

`inotifywait --event `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modify</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 이벤트만 출력하고 상태 메시지는 출력하지 않고 파일 감시:

`inotifywait --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일에 접근할 때 명령 실행:

`inotifywait --event `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">access</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` && `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>
