---
layout: page
title: osx/locate (中文)
description: "快速查找文件名。"
content_hash: 6005dc1f918f3f238a781cdb1222011030d19692
related_topics:
  - title: English version
    url: /en/osx/locate.html
    icon: bi bi-globe
---
# locate

快速查找文件名。
更多信息：<https://manned.org/locate>.

- 在数据库中查找关键字。注意：数据库定期重新更新（通常每周或每天）：

`locate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">关键字</span>

- 按文件名查找文件（不包含填充字符的模式被解释为 `*关键字*`）：

`locate */`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 重新建立文件数据索引数据库。如果要查找最近添加的文件，则需要执行此操作：

`sudo /usr/libexec/locate.updatedb`
