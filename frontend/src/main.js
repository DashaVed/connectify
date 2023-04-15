import { createApp } from 'vue'
import { createPinia } from 'pinia'
import WaveUI from 'wave-ui'
import 'wave-ui/dist/wave-ui.css'
import '@mdi/font/css/materialdesignicons.min.css'

import App from './App.vue'
import router from './router'

import './assets/main.css'

const app = createApp(App)

app.use(createPinia())
app.use(WaveUI)
app.use(router)

app.mount('#app')
