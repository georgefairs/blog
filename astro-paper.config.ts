import { defineAstroPaperConfig } from "./src/types/config";

export default defineAstroPaperConfig({
  site: {
    url: "https://georgefairs.dev/",
    title: "George Fairs",
    description:
      "Musings, research and investigations into complexity, science, and machine learning.",
    author: "George Fairs",
    profile: "https://georgefairs.dev/",
    ogImage: "default-og.jpg",
    lang: "en",
    timezone: "Europe/London",
    dir: "ltr",
  },
  posts: {
    perPage: 4,
    perIndex: 4,
    scheduledPostMargin: 15 * 60 * 1000,
  },
  features: {
    lightAndDarkMode: true,
    dynamicOgImage: true,
    showArchives: true,
    showBackButton: true,
    editPost: {
      enabled: true,
      url: "https://github.com/georgefairs/blog/edit/main/",
    },
    search: "pagefind",
  },
  socials: [
    { name: "github", url: "https://github.com/georgefairs" },
    {
      name: "linkedin",
      url: "https://www.linkedin.com/in/george-fairs-785368145/",
    },
  ],
  shareLinks: [
    { name: "linkedin", url: "https://www.linkedin.com/sharing/share-offsite/?url=" },
    { name: "whatsapp", url: "https://wa.me/?text=" },
    { name: "telegram", url: "https://t.me/share/url?url=" },
    { name: "mail", url: "mailto:?subject=See%20this%20post&body=" },
  ],
});
