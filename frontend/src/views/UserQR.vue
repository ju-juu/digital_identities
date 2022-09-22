<template>
    <div class="container">
        <center>
            <div v-if="qrData">
                <h1>Please Scan QR Code Below!</h1>
                <QRCodeDisplay :qr-data="qrData"></QRCodeDisplay>
            </div>
            <label for="psw">Enter password to validate ID</label>
            <input id="psw" type="password" placeholder="Enter Password" name="psw" required v-model="form.password">
            <button @click="refreshQR()" v-if="form.password">Generate QR Code</button>
            <button @click="home()">Home Page</button>
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