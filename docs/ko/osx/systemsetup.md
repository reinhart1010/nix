---
layout: page
title: osx/systemsetup (한국어)
description: "시스템 환경설정 기기 설정 구성."
content_hash: 851f9b759a157b4b9f685b72d2de5ca679005b73
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/systemsetup.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/osx/systemsetup.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/systemsetup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systemsetup

시스템 환경설정 기기 설정 구성.
더 많은 정보: <https://support.apple.com/guide/remote-desktop/about-systemsetup-apd95406b8d/mac>.

- 원격 로그인(SSH) 활성화:

`systemsetup -setremotelogin on`

- 시간대, NTP 서버 지정 및 네트워크 시간 활성화:

`systemsetup -settimezone "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">US/Pacific</span>`" -setnetworktimeserver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us.pool.ntp.org</span>` -setusingnetworktime on`

- 기기를 절대 절전 모드로 두지 않으며 전원 장애나 커널 패닉 시 자동으로 재시작:

`systemsetup -setsleep off -setrestartpowerfailure on -setrestartfreeze on`

- 유효한 시작 디스크 나열:

`systemsetup -liststartupdisks`

- 새로운 시작 디스크 지정:

`systemsetup -setstartupdisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
