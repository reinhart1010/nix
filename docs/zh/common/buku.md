---
layout: page
title: common/buku (中文)
description: "命令行版本的书签管理器。"
content_hash: 5b8a98b816ab75f3b6fe4f409884c1b495b3b4b7
last_modified_at: 2024-01-01
related_topics:
  - title: English version
    url: /en/common/buku.html
    icon: bi bi-globe
tldri18n_status: 2
---
# buku

命令行版本的书签管理器。
更多信息：<https://github.com/jarun/Buku>.

- 根据关键词和标签“隐私”查找书签：

`buku `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">关键词</span>` --stag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">隐私</span>

- 添加书签，并且打上标签“搜索引擎”和“隐私”：

`buku --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">搜索引擎</span>`, `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">隐私</span>

- 删除一个书签：

`buku --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">书签 id</span>

- 打开编辑器，修改书签：

`buku --write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">书签 id</span>

- 移除一个书签中的标签“搜索引擎”：

`buku --update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">书签 id</span>` --tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">搜索引擎</span>
