---
layout: page
title: common/alex (中文)
description: "捕捉文本中的不敏感、不考虑他人的写作风格。它帮助您找出文本中的性别偏向、极端化、种族相关、宗教考虑不周等不平等表达。"
content_hash: d58e0ea6ee2527f57f560770e921e6e2c4614e22
last_modified_at: 2024-06-24
related_topics:
  - title: English version
    url: /en/common/alex.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/alex.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/alex.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/alex.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/alex.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/alex.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/alex.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/alex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# alex

捕捉文本中的不敏感、不考虑他人的写作风格。它帮助您找出文本中的性别偏向、极端化、种族相关、宗教考虑不周等不平等表达。
更多信息：<https://github.com/get-alex/alex>.

- 从标准输入分析文本：

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">His network looks good</span>` | alex --stdin`

- 分析当前目录中的所有文件：

`alex`

- 分析特定文件：

`alex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.md</span>

- 分析除了 `示例文件.md` 之外的所有 Markdown 文件：

`alex *.md !`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">示例文件.md</span>
