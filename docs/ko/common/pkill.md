---
layout: page
title: common/pkill (한국어)
description: "프로세스 이름에 따라 시그널을 전송합니다."
content_hash: 9ba7099241517b6c699177b5ee21ef1d09cb9b64
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/pkill.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkill

프로세스 이름에 따라 시그널을 전송합니다.
주로 프로세스를 종료하는데 사용합니다.
더 많은 정보: <https://www.man7.org/linux/man-pages/man1/pkill.1.html>.

- 일치하는 모든 프로세스 종료:

`pkill "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>`"`

- 프로세스 이름 대신 전체 명령어와 일치하는 모든 프로세스 종료:

`pkill -f "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어_이름</span>`"`

- 강제로 일치하는 프로세스 종료 (차단 불가능):

`pkill -9 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>`"`

- 일치하는 프로세스에게 SIGUSR1 시그널 전송:

`pkill -USR1 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>`"`

- 브라우저를 닫기 위해 주요 `firefox` 프로세스를 종료:

`pkill --oldest "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firefox</span>`"`
