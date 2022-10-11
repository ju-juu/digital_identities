<template>
    <div v-if="fail">
        <center>
            <img src="src/assets/Redcross.png" alt="Success Tick" style='width: 30vh; height: 30vh;'>
        </center>
    </div>
    <div v-else-if="success">
        <center>
            <img src="src/assets/Greentick.png" alt="Success Tick" style='width: 30vh; height: 30vh;'>
        </center>
    </div>
    <div v-else>
        <StreamBarcodeReader style='width: 30vh; height: 30vh;'
                         @decode="(a, b, c) => onDecode(a, b, c)"
                         @loaded="() => onLoaded()"
    ></StreamBarcodeReader>
    </div>

    <div v-if="qrCode">
        <button @click="validateQRCode()" v-if="qrCode">Validate</button>
    </div>
</template>

<script>
import {StreamBarcodeReader} from "vue-barcode-reader";
import axios from "axios";


export default {
    name: "QRReader",
    components: {
        StreamBarcodeReader,
    },
    data() {
        return {
            qrCode: "",
            id: null,
            success: false,
            fail: false
        };
    },

    methods: {
        onDecode(a, b, c) {
            console.log(a, b, c);
            this.qrCode = a;
            if (this.id) clearTimeout(this.id);
            this.id = setTimeout(() => {
                if (this.qrCode === a) {
                    this.qrCode = "";
                }
            }, 5000);
        },
        onLoaded() {
            console.log("load");
        },
        validateQRCode() {
            console.log("Validating token: " + this.qrCode)
            axios
                .post("/validate_token", {}, {
                    headers: {
                        'Authorization': 'Bearer ' + this.qrCode
                    },
                }).then(response => {
                if (response.status === 200) {
                    console.log("Token is valid")
                    this.success = true
                } else {
                    this.success = false
                    this.fail = true
                }
            }) // #TODO if response code == 200 display tick, else cross
        },
    },
};
</script>
<style scoped>
</style>