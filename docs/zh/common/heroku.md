---
layout: page
title: common/heroku (中文)
description: "从命令行创建和管理 Heroku 应用。"
content_hash: 282f142a94909d8791ce40401d7a2fa3c3c44cea
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/heroku.html
    icon: bi bi-globe
tldri18n_status: 2
---
# heroku

从命令行创建和管理 Heroku 应用。
更多信息：<https://www.heroku.com/>.

- 登录到你的 heroku 帐户：

`heroku login`

- 创建一个 heroku 应用：

`heroku create`

- 显示应用的日志：

`heroku logs --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>

- 在 dyno（Heroku 虚拟机）中运行一次性进程：

`heroku run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>` --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>

- 列出应用的 dyno（Heroku 虚拟机）：

`heroku ps --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>

- 永久销毁应用：

`heroku destroy --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>
