import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import BaseLogo from './components/BaseLogo.vue'
import './assets/style.css'
import './axios'

const app = createApp(App)
app.component('BaseLogo', BaseLogo)

app.use(router)

app.mount('#app')
