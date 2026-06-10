---
title: "Hello, world"
pubDatetime: 2026-06-10T09:00:00Z
featured: true
draft: false
tags:
  - meta
description: "The first post on my new blog — and a quick reference for how posts are structured."
---

Welcome to my blog. This first post is here mainly as a structure reference: copy this
file, change the frontmatter, and start writing.

## Frontmatter fields

Every post starts with a frontmatter block between `---` fences:

- **title** (required) — the post title.
- **pubDatetime** (required) — publish date/time, e.g. `2026-06-10T09:00:00Z`.
- **description** (required) — short summary used for SEO and post listings.
- **tags** (optional) — a list; defaults to `["others"]` if omitted.
- **featured** (optional) — `true` shows the post in the "Featured" section on the homepage.
- **draft** (optional) — `true` hides the post from the build.
- **modDatetime** (optional) — last-modified date, shown if present.
- **author** (optional) — defaults to the site author set in `astro-paper.config.ts`.

## Writing

Below the frontmatter, write in Markdown. Headings, **bold**, _italic_, [links](https://georgefairs.dev),
lists, code blocks, and images all work out of the box.

```js
console.log("hello, world");
```

To add a new post, drop a `.md` (or `.mdx`) file into `src/content/posts/`.
