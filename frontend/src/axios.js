import axios from 'axios'

window.axios = axios
axios.defaults.baseURL = 'http://localhost:8080'
axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*'
