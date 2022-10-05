<template>
    <div class="container">
        <center>
            <div class="left"><img src="/src/assets/AB.jpeg" style='width: 30vh; height: 30vh;'></div>
        </center>
        <form>
        <div class="content">
            <div class="row">
                <div class="col"><h2>Name: </h2></div>
                <div class="col"><h3>Joe Blogs</h3></div>
            </div>
            <div class="row">
                <div class="col"><h2>D.O.B: </h2></div>
                <div class="col"><h3>14 February 2001</h3></div>
            </div>
            <div class="row">
                <div class="col"><h2>Address: </h2></div>
                <div class="col"><h3>123 Fake St</h3></div>
            </div>
            <div class="row">
                <div class="col"><h2>Number: </h2></div>
                <div class="col"><h3>081231234</h3></div>
            </div>
            <div class="row">
                <div class="col"><h2>Class: </h2></div>
                <div class="col"><h3>C, RE</h3></div>
            </div>
        </div></form>
        <button class="button button2" @click="verifyQR()" style="width: 100%" align="center">Verify</button>
        <button class="button button2"  style="width: 100%" align="center">Add a New ID</button>
        <button class="button button2" @click="logout()" style="width: 100%" align="center">Logout</button>
    </div>
</template>
<script>
import router from "../router";

export default {
    name: 'userHome',
    methods: {
        verifyQR() {
            router.push('/user_qr')
        },
        logout() {
            router.push('/')
        }
    },
}
</script>