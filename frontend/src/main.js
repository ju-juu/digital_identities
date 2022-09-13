import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import BaseLogo from './components/BaseLogo.vue'
import './assets/style.css'
import './axios'
// import QRreader from "./components/QRreader";
const app = createApp(App)


app.component('BaseLogo', BaseLogo)

// app.component('QRreader', QRreader)

app.use(router)

app.mount('#app')
