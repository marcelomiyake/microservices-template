import { defineConfig } from 'vitest/config'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: { '/api': 'http://127.0.0.1:8081' },
  },
  test: {
    include: ['src/**/*.spec.ts'],
    environment: 'jsdom',
    clearMocks: true,
    coverage: {
      provider: 'v8',
      include: ['src/App.vue', 'src/main.ts'],
      exclude: ['src/**/*.spec.ts'],
      reporter: ['text', 'lcov'],
      reportsDirectory: 'coverage',
    },
  },
})
