<template>
    <div class="container">
        <BaseLogo/>
        <BaseLoginForm :form="this.form"/>
    </div>
</template>
<script>

import BaseLoginForm from "../components/BaseLoginForm.vue";

export default {
    components: {BaseLoginForm},
    data() {
        return {
            form: {
                email: '',
                password: ''
            }
        }
    },
}
</script>