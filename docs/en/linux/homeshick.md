---
layout: page
title: linux/homeshick (English)
description: "Synchronize Git dotfiles."
content_hash: 3e826c702481b019d9c33e025733360e8c47403b
---
# homeshick

Synchronize Git dotfiles.
More information: <https://github.com/andsens/homeshick/wiki>.

- Create a new castle:

`homeshick generate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">castle_name</span>

- Add a file to your castle:

`homeshick track `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">castle_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Go to a castle:

`homeshick cd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">castle_name</span>

- Clone a castle:

`homeshick clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github_username</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_name</span>

- Symlink all files from a castle:

`homeshick link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">castle_name</span>
