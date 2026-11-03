import { defineConfig } from 'astro/config';

export default defineConfig({
  output: 'static',
  site: 'https://karetnikov-family.pages.dev',
  build: {
    assets: 'assets_heritage',
    inlineStylesheets: 'always'
  },
  server: {
    port: 4328,
    host: true
  }
});
