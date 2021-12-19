---
layout: page
title: linux/sensible-editor (English)
description: "Open the default editor."
content_hash: f93ddfd43741831ed4a28dc7be3c08f715b4eaed
---
# sensible-editor

Open the default editor.

- Open a file in the default editor:

`sensible-editor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Open a file in the default editor, with the cursor at the end of the file:

`sensible-editor + `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Open a file in the default editor, with the cursor at the beginning of line 10:

`sensible-editor +10 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Open 3 files in vertically split editor windows at the same time:

`sensible-editor -O3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_3</span>
