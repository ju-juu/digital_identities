<template>
    <form @submit.prevent="userLogin()">
        <label for="email"><b>Email Address</b></label>
        <input id="email" type="text" placeholder="Enter Email Address" name="email" required v-model="form.email">
        <label for="psw"><b>Password</b></label>
        <input id="psw" type="password" placeholder="Enter Password" name="psw" required v-model="form.password">
        <button type="submit">Login</button>
        <label>
            <input type="checkbox" checked="checked" name="remember"> Remember me
        </label>
        <div class="container" style="background-color:#f1f1f1">
            <span class="psw1"><a href="#">Create an Account</a></span>
            <span class="psw2"><a href="#">Forgot Password?</a></span>
        </div>
    </form>
</template>
<script>
import axios from 'axios'
import router from "../router";

export default {
    props: ['form'],
    methods: {
        userLogin() {
            axios.post('/user/login', this.form).then(resp => {

                router.push('/user_home')
            });
        }
    }
}
</script>