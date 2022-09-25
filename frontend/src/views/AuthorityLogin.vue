<template>
    <div class="container">
        <BaseLogo/>
        <form @submit.prevent="authLogin()">
            <label for="email"><b>Email Address</b></label>
            <input id="email" type="text" placeholder="Enter Email Address" name="email" required v-model="form.email">
            <label for="psw"><b>Password</b></label>
            <input id="psw" type="password" placeholder="Enter Password" name="psw" required v-model="form.password">
            <button type="submit">Login</button>
            <label>
                <input type="checkbox" checked="checked" name="remember"> Remember me
            </label>
        </form>
    </div>
</template>
<script>

import axios from "axios";
import router from "../router";

export default {
    data() {
        return {
            form: {
                email: '',
                password: ''
            }
        }
    },
    methods: {
        authLogin() {
            axios.post('/user/login', this.form).then(() => {
                router.push('authority_home')
            });
        }
    }
}
</script>