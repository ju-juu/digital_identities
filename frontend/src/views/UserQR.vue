<template>
    <div class="container">
        <h1>Please Scan QR Code Below!</h1>
        <center>
            <QRCodeDisplay v-if="qrData" :qr-data="qrData"></QRCodeDisplay>
            <label for="psw"><p>Enter Password</p></label>
            <input id="psw" type="password" placeholder="Enter Password" name="psw" required v-model="form.password">
            <button @click="refreshQR()" v-if="form.password">Generate QR Code</button>
            <button @click.prevent="home()">Home Page</button>
        </center>
    </div>
</template>
<script>
import axios from 'axios';
import QRCodeDisplay from "../components/QRCodeDisplay.vue";
import router from "../router";

export default {
    components: {
        QRCodeDisplay
    },
    data() {
        return {
            form: {
                email: 'test@test.com',
                password: ''
            },
            qrData: null
        }
    },
    methods: {
        refreshQR() {
            axios.post('/user/login', this.form).then(resp => {
                this.qrData = resp.data['access_token']
            });
        },
        home() {
            router.push('/user_home')
        }

    }
}
</script>