---
layout: page
title: common/pocount (English)
description: "Translate Toolkit utility to get translation progress from file, supporting several formats."
content_hash: 3c355d697fca5f5d8725a43697f99e34868990e3
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/pocount.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pocount

Translate Toolkit utility to get translation progress from file, supporting several formats.
More information: <https://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/pocount.html>.

- Print a colorful table with the translation progress of a file:

`pocount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file/file.po</span>

- Print translation progress of various files, one line per file:

`pocount --short `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">translation_*.ts</span>

- Generate a CSV file with the translation progress of various files:

`pocount --csv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">translation_*.ts</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/translation_progress.csv</span>
