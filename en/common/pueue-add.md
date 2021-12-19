---
layout: page
title: common/pueue-add (English)
description: "Enqueue a task for execution."
content_hash: 93a79972d3f5b76805940ca702b4b2088e7f5693
---
# pueue add

Enqueue a task for execution.
More information: <https://github.com/Nukesor/pueue>.

- Add any command to the default queue:

`pueue add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Pass a list of flags or arguments to a command when enqueuing:

`pueue add -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command --arg -f</span>

- Add a command but do not start it if it's the first in a queue:

`pueue add --stashed -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rsync --archive --compress /local/directory /remote/directory</span>

- Add a command to a group and start it immediately, see `pueue group` to manage groups:

`pueue add --immediate --group "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CPU_intensive</span>`" -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ffmpeg -i input.mp4 frame_%d.png</span>

- Add a command and start it after commands 9 and 12 finish successfully:

`pueue add --after `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">12</span>` --group "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">torrents</span>`" -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">transmission-cli torrent_file.torrent</span>

- Add a command with a label after some delay has passed, see `pueue enqueue` for valid datetime formats:

`pueue add --label "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compressing large file</span>`" --delay "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wednesday 10:30pm</span>`" -- "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7z a compressed_file.7z large_file.xml</span>`"`
