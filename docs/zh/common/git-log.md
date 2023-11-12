---
layout: page
title: common/git-log (中文)
description: "查看提交历史。"
content_hash: 15fcc8da794b13ff0b985c46c401ed2a3447b5a8
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-log.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-log.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-log.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-log.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-log.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-log.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-log.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git log

查看提交历史。
更多信息：<https://git-scm.com/docs/git-log>.

- 按时间先后顺序列出当前仓库所有的提交，最近的更新排在最上面：

`git log`

- 查看指定文件或指定目录的历史，包括每次提交所引入的差异：

`git log -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件或目录</span>

- 显示每次提交的文件修改统计信息：

`git log --stat`

- 在日志旁以 ASCII 图形显示当前分支提交历史，并只展示提交消息的第一行：

`git log --oneline --graph`

- 在日志旁以 ASCII 图形显示整个仓库的所有提交、标签、分支：

`git log --oneline --decorate --all --graph`

- 查看提交消息中包含特定字符串（大小写敏感）的提交：

`git log -i --grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字符串</span>

- 查看特定作者的最近 N 条提交：

`git log -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">数字</span>` --author=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">作者</span>

- 查看两个日期之间的提交（yyyy-mm-dd）：

`git log --before="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2017-01-29</span>`" --after="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2017-01-17</span>`"`
