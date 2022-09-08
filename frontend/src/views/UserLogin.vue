<template>
    <div class="container">
        <BaseLogo/>
        <h1>User Login Page</h1>
        <form onsubmit="testLog()">
            <label for="email"><b>Email Address</b></label>
            <input id="email" type="text" placeholder="Enter Email Address" name="email" required>
            <label for="psw"><b>Password</b></label>
            <input id="psw" type="password" placeholder="Enter Password" name="psw" required>
            <button type="submit">Login</button>
            <label>
                <input type="checkbox" checked="checked" name="remember"> Remember me
            </label>
            <div class="container" style="background-color:#f1f1f1">
                <span class="psw1"><a href="#">Create an Account</a></span>
                <span class="psw2"><a href="#">Forgot Password?</a></span>
            </div>
        </form>
    </div>
</template>