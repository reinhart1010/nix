---
layout: page
title: windows/reg-add (中文)
description: "将新的键值添加到注册表中。"
content_hash: 076f652d589f3e745f8e56344acb0979739c3e12
related_topics:
  - title: English version
    url: /en/windows/reg-add.html
    icon: bi bi-globe
---
# reg add

将新的键值添加到注册表中。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/reg-add>.

- 添加一个新的注册表键：

`reg add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名</span>

- 在指定的键下添加新值：

`reg add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名</span>` /v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">值</span>

- Add a new value with specific data：

`reg add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名</span>` /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">数据</span>

- 向具有特定数据类型的键添加新值：

`reg add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名</span>` /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">类型</span>

- 在没有提示的情况下强制覆盖现有的注册表值：

`reg add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名</span>` /f`
