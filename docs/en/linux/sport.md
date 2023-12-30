---
layout: page
title: linux/sport (English)
description: "Search and install SlackBuilds."
content_hash: 057290a76c2c1981b71755be5105ad1ca43f4bec
last_modified_at: 2023-12-30
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/sport.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sport

Search and install SlackBuilds.
More information: <http://slackermedia.info/handbook/doku.php?id=slackbuilds>.

- Pull the list of SlackBuilds to run `sport` for the first time:

`sudo mkdir -p /usr/ports && sudo rsync -av rsync://slackbuilds.org /slackbuilds/$(awk '{print $2}' /etc/slackware-version)/ /usr/ports/`

- Pull in any updates to the system's tree via `rsync`:

`sudo sport rsync`

- Search for a package by name:

`sport search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>`"`

- Check if a package is installed:

`sport check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Display README and `.info` files of a package:

`sport cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Install a package once the dependencies are resolved:

`sudo sport install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Install a list of packages from a file (format: packages separated by spaces):

`sudo sport install $(< `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/list</span>`)`
