import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios'
import WaveUI from 'wave-ui'
import 'wave-ui/dist/wave-ui.css'
import '@mdi/font/css/materialdesignicons.min.css'

import App from './App.vue'
import router from './router'

import './assets/main.css'

axios.defaults.xsrfCookieName = "csrftoken"
axios.defaults.xsrfHeaderName = "X-CSRFToken"

const app = createApp(App)

app.use(createPinia())
app.use(WaveUI)
app.use(router, axios)

app.mount('#app')
