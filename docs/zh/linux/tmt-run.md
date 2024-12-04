---
layout: page
title: linux/tmt-run (中文)
description: "执行测试步骤。默认情况下，所有测试步骤都被执行。"
content_hash: ab914a3e904cf2f000dfb0cbc6b0e35e7c005405
last_modified_at: 2024-12-04
related_topics:
  - title: English version
    url: /en/linux/tmt-run.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/tmt-run.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tmt run

执行测试步骤。默认情况下，所有测试步骤都被执行。
更多信息：<https://tmt.readthedocs.io/en/stable/overview.html#run>.

- 在每一个计划中执行所有测试步骤：

`tmt run`

- 仅在发现步骤中显示将要执行的测试：

`tmt run discover -v`

- 运行所有测试步骤并调整测试环境配置步骤选项：

`tmt run --all provision --how `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>` --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fedora:rawhide</span>

- 仅执行选定的计划和测试：

`tmt run plan --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/plan/name</span>` test --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/test/name</span>

- 在网页浏览器中显示上次运行的结果：

`tmt run --last report --how `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html</span>` --open`

- 在提供的上下文中运行测试：

`tmt run --context `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key=value</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">distro=fedora</span>

- 以交互方式运行测试（在测试运行过程中调试测试代码）：

`tmt run --all execute --how `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmt</span>` --interactive`

- 使用干模式查看接下来将发生的动作，并将输出详实度设置为最高级：

`tmt run --dry -vvv`
