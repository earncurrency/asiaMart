import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    // vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  define: {
    __BASE_URL__: JSON.stringify('http://localhost/asiaMart'),
    // __API_BASE_URL__: JSON.stringify('https://api.example.com'),
  },
})

// export default {
//   mounted() {
//     console.log(__API_BASE_URL__); // Output: "https://api.example.com"
//     console.log(__APP_NAME__);    // Output: "My Awesome App"
//     console.log(__VERSION__);     // Output: "1.0.0"
//   }
// };