---
layout: page
title: common/gifsicle (English)
description: "Create GIFs."
content_hash: 437384b64d81ba640c528215799a5d5406ffa6d9
---
# gifsicle

Create GIFs.
More information: <https://www.lcdf.org/gifsicle>.

- Optimise a GIF:

`gifsicle --batch --optimize=3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">amin.gif</span>

- Make a GIF animation with gifsicle:

`gifsicle --delay=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --loop *.gif > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anim.gif</span>

- Extract frames from an animation:

`gifsicle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anim.gif</span>` '#0' > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firstframe.gif</span>

- You can also edit animations by replacing, deleting, or inserting frames:

`gifsicle -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anim.gif</span>` --replace '#0' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new.gif</span>
