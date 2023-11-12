---
layout: page
title: common/crontab (한국어)
description: "현재 사용자의 시간 간격으로 cron작업이 실행되도록 스케줄."
content_hash: 00fc6feca61f89a3593b24757cb00320d1e5a04c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/crontab.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/crontab.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/crontab.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># crontab

현재 사용자의 시간 간격으로 cron작업이 실행되도록 스케줄.
작업 정의 형식: "(분) (시) (날짜) (달) (요일) 실행 할 명령".
더 많은 정보: <https://crontab.guru/>.

- 현재 사용자의 crontab파일 편집:

`crontab -e`

- 특정 사용자에 대한 crontab파일 편집:

`sudo crontab -e -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>

- 현재 사용자의 기존 cron작업 목록 보기:

`crontab -l`

- 현재 사용자의 모든 cron작업 제거:

`crontab -r`

- 매일 10:00에 실행되는 샘플 작업 (* 은 모든 값을 의미 함):

`0 10 * * * `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">실행_할_명령</span>

- 4월 3일에 1분마다 실행되는 샘플 작업:

`* * 3 Apr * `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">실행_할_명령</span>

- 매주 금요일 02:30에 특정 스크립트를 실행하는 샘플 작업:

`30 2 * * Fri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/script.sh/의/절대/경로</span>
