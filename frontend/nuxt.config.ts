import { defineNuxtConfig } from 'nuxt'

export default defineNuxtConfig({
  telemetry: false,
  meta: {
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
    ],
  },
  css: [
    '@/assets/style.css',
  ],
  buildModules: [
    'nuxt-windicss',
  ],
})
