<template>
    <qrcode-vue :value="value" :size="size" level="H"/>
</template>
<script>
import QrcodeVue from 'qrcode.vue'

export default {
    props: ['qrData'],
    data() {
        return {
            value: this.qrData,
            size: 300,
        }
    },
    components: {
        QrcodeVue,
    },
}
</script>