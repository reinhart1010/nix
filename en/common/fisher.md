---
layout: page
title: common/fisher (English)
description: "Fisher, a fish-shell plugin manager."
content_hash: 70bd7738351d3d6124a496e09a9b170ba4dc1782
---
# fisher

Fisher, a fish-shell plugin manager.
Install plugins by name or from a managed 'fishfile' for bundled installs.
More information: <https://github.com/jorgebucaran/fisher>.

- Install one or more plugins:

`fisher `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin2</span>

- Install a plugin from a GitHub gist:

`fisher `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gist_url</span>

- Edit 'fishfile' manually with your favorite editor and install multiple plugins:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">editor</span>` ~/.config/fish/fishfile; fisher`

- List installed plugins:

`fisher ls`

- Update plugins:

`fisher update`

- Remove one or more plugins:

`fisher remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin2</span>
