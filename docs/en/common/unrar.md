---
layout: page
title: common/unrar (English)
description: "Extract RAR archives."
content_hash: 87a1214bf1b922c73e56124086fb903ae1cf7864
related_topics:
  - title: español version
    url: /es/common/unrar.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/unrar.html
    icon: bi bi-globe
---
# unrar

Extract RAR archives.
More information: <https://manned.org/unrar>.

- Extract files with original directory structure:

`unrar x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compressed.rar</span>

- Extract files to a specified path with the original directory structure:

`unrar x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compressed.rar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/extract</span>

- Extract files into current directory, losing directory structure in the archive:

`unrar e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compressed.rar</span>

- Test integrity of each file inside the archive file:

`unrar t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compressed.rar</span>

- List files inside the archive file without decompressing it:

`unrar l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compressed.rar</span>
