---
layout: page
title: linux/hostnamectl (한국어)
description: "컴퓨터의 호스트명을 가져오거나 설정합니다."
content_hash: d0c81d8f3caf527f0954a9c8f039a7f37eb29d74
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/hostnamectl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/hostnamectl.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/linux/hostnamectl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hostnamectl

컴퓨터의 호스트명을 가져오거나 설정합니다.
더 많은 정보: <https://manned.org/hostnamectl>.

- 컴퓨터의 호스트명 가져오기:

`hostnamectl`

- 컴퓨터의 호스트명 설정:

`sudo hostnamectl set-hostname "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>`"`

- 컴퓨터에 보기 좋은 호스트명 설정:

`sudo hostnamectl set-hostname --static "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명.example.com</span>`" && sudo hostnamectl set-hostname --pretty "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>`"`

- 호스트명을 기본값으로 재설정:

`sudo hostnamectl set-hostname --pretty ""`
