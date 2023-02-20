---
layout: page
title: osx/systemsetup (English)
description: "Configure System Preferences machine settings."
content_hash: 2098419abc0f2c186c08e02ae1f279f7d2adcdb9
last_modified_at: 2023-02-20
related_topics:
  - title: português (Portugal) version
    url: /pt_PT/osx/systemsetup.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/systemsetup.html
    icon: bi bi-globe
---
# systemsetup

Configure System Preferences machine settings.
More information: <https://support.apple.com/guide/remote-desktop/about-systemsetup-apd95406b8d/mac>.

- Enable remote login (SSH):

`systemsetup -setremotelogin on`

- Specify timezone, NTP Server and enable network time:

`systemsetup -settimezone "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">US/Pacific</span>`" -setnetworktimeserver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us.pool.ntp.org</span>` -setusingnetworktime on`

- Make the machine never sleep and automatically restart on power failure or kernel panic:

`systemsetup -setsleep off -setrestartpowerfailure on -setrestartfreeze on`

- List valid startup disks:

`systemsetup -liststartupdisks`

- Specify a new startup disk:

`systemsetup -setstartupdisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
