---
layout: page
title: common/gitmoji (English)
description: "An interactive command-line tool for using emojis on commits."
content_hash: 01ec30ab9d131477e5f22508258708756f91613d
last_modified_at: 2024-01-30
related_topics:
  - title: 한국어 version
    url: /ko/common/gitmoji.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/gitmoji.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gitmoji

An interactive command-line tool for using emojis on commits.
More information: <https://github.com/carloscuesta/gitmoji-cli>.

- Start the commit wizard:

`gitmoji --commit`

- Initialize the Git hook (so `gitmoji` will be run every time `git commit` is run):

`gitmoji --init`

- Remove the Git hook:

`gitmoji --remove`

- List all available emojis and their descriptions:

`gitmoji --list`

- Search emoji list for a list of keywords:

`gitmoji --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword2</span>

- Update cached list of emojis from main repository:

`gitmoji --update`

- Configure global preferences:

`gitmoji --config`
