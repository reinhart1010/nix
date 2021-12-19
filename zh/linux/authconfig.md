---
layout: page
title: linux/authconfig (中文)
description: "用于设置系统认证资源的命令行界面。"
content_hash: d64975a32769af269f638a3eb775410f72c78cef
related_topics:
  - title: English version
    url: /en/linux/authconfig.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/authconfig.html
    icon: bi bi-globe
---
# authconfig

用于设置系统认证资源的命令行界面。
更多信息：<https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system-level_authentication_guide/authconfig-install>.

- 显示当前的配置（或空运行）：

`authconfig --test`

- 设置服务器使用另一种不同的密码散列算法：

`authconfig --update --passalgo=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">算法名</span>

- 启用 LDAP 认证：

`authconfig --update --enableldapauth`

- 关闭 LDAP 认证：

`authconfig --update --disableldapauth`

- 开启网络信息服务（NIS）：

`authconfig --update --enablenis`

- 开启 Kerberos:

`authconfig --update --enablekrb5`

- 开启 Winbind（活动目录）认证：

`authconfig --update --enablewinbindauth`

- 开启本地认证：

`authconfig --update --enablelocauthorize`
