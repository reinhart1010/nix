---
layout: page
title: linux/addr2line (中文)
description: "将二进制文件地址转换成文件名和行数。"
content_hash: 7e840e51e11a1ab2d0acc9aa21e81c3256d1d9cd
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/addr2line.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/addr2line.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/addr2line.html
    icon: bi bi-globe
tldri18n_status: 2
---
# addr2line

将二进制文件地址转换成文件名和行数。
更多信息：<https://manned.org/addr2line>.

- 显示可执行文件的指令地址对应源代码的文件名和行数：

`addr2line --exe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">可执行文件路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">地址</span>

- 显示函数名、文件名和行数：

`addr2line --exe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">可执行文件路径</span>` --functions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">地址</span>

- 将 C++ 代码函数名符号重组：

`addr2line --exe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">可执行文件地址</span>` --functions --demangle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">地址</span>
