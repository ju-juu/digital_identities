<template>
    <div class="container">
        <h1>Point At QR Code</h1>
        <div>
            <center>
                <QRReader style="height: 400px; width: 400px"></QRReader>
            </center>
        </div>
        <div>
            <button class="button button2" @click="help()" style="width: 100%" align="center">Help</button>
            <button class="button button2" @click="logout()" style="width: 100%" align="center">Logout</button>
        </div>
    </div>
</template>
<script>
import QRReader from "../components/QRReader.vue";
import router from "../router";

export default {
    components: {QRReader},
    name: 'AuthorityHome',
    methods: {
        logout() {
            router.push('/')
        },
        help() {
            router.push('/authority_help')
        }
    },
}
</script>