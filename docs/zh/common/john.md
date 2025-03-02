---
layout: page
title: common/john (中文)
description: "密码破解工具。"
content_hash: 4933f21ffda3e30ac8e278eecb78fc2a45fc25df
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/john.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/john.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/john.html
    icon: bi bi-globe
tldri18n_status: 2
---
# john

密码破解工具。
更多信息：<https://www.openwall.com/john/>.

- 破解密码哈希：

`john `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/hashes.txt</span>

- 显示已破解的密码：

`john --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/hashes.txt</span>

- 按用户标识符从多个文件中显示用户的已破解密码：

`john --show --users=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户_IDs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/hashes1.txt 路径/到/hashes2.txt ...</span>

- 使用自定义的单词列表破解密码哈希：

`john --wordlist=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/wordlist.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/hashes.txt</span>

- 列出可用的哈希格式：

`john --list=formats`

- 使用特定的哈希格式破解密码哈希：

`john --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">md5crypt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/hashes.txt</span>

- 启用单词变形规则破解密码哈希：

`john --rules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/hashes.txt</span>

- 从状态文件恢复一个中断的破解会话，例如：`mycrack.rec`：

`john --restore=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/mycrack.rec</span>
