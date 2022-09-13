<template>
    <h1>Welcome</h1>
    <form action="...." method="post">
        <div class="exwrapper">
            <div class="wrapper">
                <div class="left"><img src="AB.jpeg" style='width: 100%'></div>
                <div class="content">
                    <p1>Driving Licence</p1>
                    <h2>Full Name: </h2>
                    <h2>Date of Birth: </h2>
                    <h2>Address: </h2>
                    <h2>Licence Class: </h2>
                    <h2>Licence Number: </h2>
                </div>
                <button class="button button2" @click="verifyQR" type="Verify The Card" style="width: 100%" align="center">Verify The
                    Card
                </button>
            </div>
        </div>
    </form>
</template>
<script>
    import router from "../router";

    export default {
        methods: {
            verifyQR() {
                router.push('user_qr')
            }
        }
    }
</script>