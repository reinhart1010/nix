---
layout: page
title: common/ntfyme (한국어)
description: "장기 실행 종료 프로세스를 추적하고 알림을 보내는 알림 도구."
content_hash: eb58f3ece5f32cd2b7baf901c07322b0d6d0cefc
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ntfyme.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ntfyme

장기 실행 종료 프로세스를 추적하고 알림을 보내는 알림 도구.
Gmail, Telegram 등을 통해 성공/오류 메시지로 알림을 전송.
더 많은 정보: <https://github.com/AnirudhG07/ntfyme>.

- 명령어를 직접 실행:

`ntfyme exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--cmd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 명령어를 파이프로 전달하여 실행:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | ntfyme exec`

- 여러 명령어를 큰따옴표로 묶어 실행:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어1; 명령어2; 명령어3</span>`" | ntfyme exec`

- 장기 중단 후 프로세스를 추적하고 종료:

`ntfyme exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--track-process</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--cmd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 도구 구성을 대화식으로 설정:

`ntfyme setup`

- 비밀번호 암호화:

`ntfyme enc`

- 로그 기록 보기:

`ntfyme log`

- 구성 파일 열기 및 편집:

`ntfyme config`
