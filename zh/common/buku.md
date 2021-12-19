---
layout: page
title: common/buku (中文)
description: "命令行版本的书签管理器。"
content_hash: 6c89b29cda88c19c0bcf1fe54994cb46bb55b2c9
related_topics:
  - title: English version
    url: /en/common/buku.html
    icon: bi bi-globe
---
# buku

命令行版本的书签管理器。
更多信息：<https://github.com/jarun/Buku>.

- 根据关键词和标签查找书签：

`buku `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">关键字</span>` --stag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">标签</span>

- 添加书签，并且打上标签：

`buku --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">搜索引擎</span>`, `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">标签</span>

- 删除一个书签：

`buku --delete "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">书签 id</span>`"`

- 打开编辑器，修改书签：

`buku --write "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">书签 id</span>`"`

- 将指定标签移除：

`buku --update "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">书签 id</span>`" --tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">搜索引擎</span>
