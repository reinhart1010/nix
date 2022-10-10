---
layout: page
title: common/vale (English)
description: "Extensible style checker that supports multiple markup formats, such as Markdown and AsciiDoc."
content_hash: 595b950745b61d746e08e8fedbf76d2d37a6bfbc
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># vale

Extensible style checker that supports multiple markup formats, such as Markdown and AsciiDoc.
More information: <https://vale.sh>.

- Check the style of a file:

`vale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Check the style of a file with a specified configuration:

`vale --config='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/.vale.ini</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Output the results in JSON format:

`vale --output=JSON `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Check style issues at the specific severity and higher:

`vale --minAlertLeve=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suggestion|warning|error</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Check the style from stdin, specifying markup format:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.md</span>` | vale --ext=.md`

- List the current configuration:

`vale ls-config`
