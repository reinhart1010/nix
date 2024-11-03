---
layout: page
title: common/bdfr (English)
description: "Bulk downloader for Reddit."
content_hash: f71f85ed729273c2bf6ccdd0e73b777882ad2b86
last_modified_at: 2024-11-03
tldri18n_status: 2
---
# bdfr

Bulk downloader for Reddit.
More information: <https://github.com/Serene-Arc/bulk-downloader-for-reddit>.

- Download videos/images from the specified [l]inks to URL or ID's of posts:

`bdfr download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_directory</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">post_url</span>

- Download the maximum possible number (roughly 1000) of videos/images from a specified [u]ser:

`bdfr download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_directory</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reddit_user</span>` --submitted`

- Download submission data (text, upvotes, comments, etc.) [L]imited to 10 submissions for each [s]ubreddit (30 total):

`bdfr archive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_directory</span>` -s '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Python, all, mindustry</span>`' -L 10`

- Download videos/images from the [s]ubreddit r/Python [S]orted by top (default is hot) using [t]ime filter all, [L]imited to 10 submissions:

`bdfr download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_directory</span>` -s Python -S top -t all -L 10`

- Download the maximum possible number of both submission data and videos/images from [s]ubreddit r/Python skipping over submissions with mp4 or gif file extensions and creating hard links for duplicate files:

`bdfr clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_directory</span>` -s Python --skip mp4 --skip gif --make-hard-links`

- Download saved posts of the authenticated user, naming each file according to a specified format. Avoid downloading duplicates and posts already present in the output directory:

`bdfr download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_directory</span>` --user me --saved --authenticate --file-scheme '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"> {POSTID}_{TITLE}_{UPVOTES} </span>`' --no-dupes --search-existing`
