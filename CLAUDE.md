# CLAUDE.md

Personal blog for **georgefairs.dev**, built on the [AstroPaper](https://github.com/satnaing/astro-paper) theme (Astro 6 + Tailwind).

## Project facts

- **Package manager:** npm (the pnpm lockfiles were removed). Vite is pinned to `^7` via `overrides` in `package.json` because Astro 6 rejects Vite 8.
- **Config:** edit `astro-paper.config.ts` (site title, description, author, socials, features). `src/config.ts` just resolves defaults — don't edit it.
- **Theme/colours:** `src/styles/theme.css` — seven CSS variables per block (`:root` = light, `[data-theme="dark"]` = dark). Currently "Minimal Mono".
- **Font:** JetBrains Mono, configured in `astro.config.ts` (the `fonts:` block). The css variable `--font-jetbrains-mono` is referenced in `astro-paper.config.ts`'s consumer files (`Layout.astro`, `og.png.ts`, `posts/[...slug]/index.png.ts`) — keep all in sync if changing it.

## Commands

| Command | Purpose |
|---|---|
| `npm run dev` | Dev server at http://localhost:4321 (hot-reloads CSS/content; restart for `astro.config.ts` changes) |
| `npm run build` | Production build: `astro check` + build + Pagefind search index |
| `npm run format` | Auto-format with Prettier (run before committing) |
| `npm run lint` | ESLint |

## Deployment

Push to `main` → GitHub Actions (`.github/workflows/deploy.yml`) builds and deploys to GitHub Pages → live at https://georgefairs.dev (~1 min). No manual step. Custom domain + TLS are handled by GitHub Pages; `public/CNAME` holds the domain.

## Creating a new post

Posts live in `src/content/posts/` as `.md` (or `.mdx` if you need components).

1. **Create the file.** The **filename becomes the URL slug** — there is no `slug` frontmatter field. `src/content/posts/my-first-idea.md` → `/posts/my-first-idea`. Subfolders become URL segments (`posts/notes/foo.md` → `/posts/notes/foo`); folders/files starting with `_` are ignored.

2. **Add frontmatter.** Required: `title`, `pubDatetime`, `description`. Everything else is optional:

   ```yaml
   ---
   title: "My post title"
   pubDatetime: 2026-06-11T09:00:00Z   # required; use Europe/London-aware time
   description: "One-sentence summary for SEO and post listings."
   tags:                                # optional; defaults to ["others"]
     - complexity
     - ml
   featured: false                      # optional; true = pin to homepage "Featured"
   draft: false                         # optional; true = never built/published
   # modDatetime: 2026-06-12T00:00:00Z  # optional; shows "last updated"
   # ogImage: "@/assets/images/foo.png" # optional; otherwise an OG image is auto-generated
   # author: "George Fairs"             # optional; defaults to site author
   ---
   ```

3. **Write the body** in Markdown below the frontmatter.

4. **Images:** put them in `src/assets/images/` and reference with `![alt](@/assets/images/file.png)` (these get optimized at build). Use `public/` only for files you want served verbatim (reference as `/file.png`).

5. **Preview:** `npm run dev`. Note the filtering rules (`src/utils/postFilter.ts`):
   - `draft: true` → always hidden (dev and prod).
   - A future `pubDatetime` → **scheduled**: hidden in production until that time, but visible in `dev` so you can preview.

6. **Publish:** make sure `draft` is `false` (or absent) and `pubDatetime` is now/past. Then:

   ```bash
   npm run format        # so CI's format:check passes
   npm run build         # catch errors before pushing
   git add -A && git commit -m "post: my first idea" && git push
   ```

   The push to `main` auto-deploys. The post appears at `georgefairs.dev/posts/<filename>`.

See `src/content/posts/hello-world.md` for a working reference.
