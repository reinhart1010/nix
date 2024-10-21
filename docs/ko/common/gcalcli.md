---
layout: page
title: common/gcalcli (한국어)
description: "Google 캘린더와 상호작용."
content_hash: 76bb55ca34107ae6304f86d9bd5055678d609c3e
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/gcalcli.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/gcalcli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcalcli

Google 캘린더와 상호작용.
처음 실행 시 Google API 인증을 요청.
더 많은 정보: <https://github.com/insanum/gcalcli>.

- 향후 7일 동안의 모든 캘린더에 대한 이벤트를 나열:

`gcalcli agenda`

- 특정 날짜부터 또는 그 사이에 시작되는 이벤트 표시(예: "내일"과 같은 상대 날짜도 사용):

`gcalcli agenda `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mm/dd</span>` [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mm/dd</span>`]`

- 특정 캘린더의 이벤트 나열:

`gcalcli --calendar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">캘린더_이름</span>` agenda`

- 주별 이벤트의 ASCII 달력을 표시:

`gcalcli calw`

- 한 달 동안의 이벤트에 대한 ASCII 달력을 표시:

`gcalcli calm`

- 캘린더에 이벤트를 빠르게 추가:

`gcalcli --calendar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">캘린더_이름</span>` quick "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mm/dd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HH:MM</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이벤트_이름</span>`"`

- 캘린더에 이벤트를 추가. 대화형 프롬프트를 트리거:

`gcalcli --calendar "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">캘린더_이름</span>`" add`
