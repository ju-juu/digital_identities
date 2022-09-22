<template>
    <div class="container">
        <center>
            <div class="left"><img src="src/assets/AB.jpeg" style='width: 30vh; height: 30vh;'></div>
        </center>
        <div class="content">
            <h1>Drivers Licence</h1>
            <h2>Full Name: </h2>
            <h2>Date of Birth: </h2>
            <h2>Address: </h2>
            <h2>Licence Class: </h2>
            <h2>Licence Number: </h2>
        </div>
        <button class="button button2" @click.prevent="verifyQR()" style="width: 100%" align="center">Verify
        </button>
    </div>
</template>
<script>
import router from "../router";

export default {
    props: ['email'],
    name: 'userHome',
    methods: {
        verifyQR() {
            router.push('/user_qr')
        }
    },
    created() {
        console.log('created')
        console.log(this.email)
    }
}
</script>