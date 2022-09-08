<template>
    <div class="container">
        <BaseLogo/>
        <h1>Authority Login Page</h1>
        <form action="...." method="post">
            <label for="email"><b>Email Address</b></label>
            <input id="email" type="text" placeholder="Enter Email Address" name="email" required>
            <label for="psw"><b>Password</b></label>
            <input id="psw" type="password" placeholder="Enter Password" name="psw" required>
            <button type="submit">Login</button>
            <label>
                <input type="checkbox" checked="checked" name="remember"> Remember me
            </label>
        </form>
    </div>
</template>
<script>

</script>