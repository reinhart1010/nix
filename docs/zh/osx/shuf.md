---
layout: page
title: osx/shuf (中文)
description: "生成随机排列。"
content_hash: 878e9576133f6c103a9f6ab6a8b67e49ccd7d455
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/shuf.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/shuf.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/shuf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shuf

生成随机排列。
更多信息：<https://www.unix.com/man-page/linux/1/shuf/>.

- 随机化文件中的行顺序并输出结果：

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 只输出结果的前 5 条：

`shuf -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 将结果输出写入另一个文件：

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">输出_文件名</span>

- 生成范围（1-10）内的随机数：

`shuf -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-10</span>
