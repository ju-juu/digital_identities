<template>
    <div v-if="fail">
        <center>
            <img src="src/assets/Redcross.png" alt="Fail Cross" style='width: 30vh; height: 30vh;'>
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
        async validateQRCode() {
            console.log("Validating token: " + this.qrCode)
            try {
                const response = await axios
                    .post("/validate_token", {}, {
                        headers: {
                            'Authorization': 'Bearer ' + this.qrCode
                        },
                    }).then(response => {
                        if (response.status === 200) {
                            console.log("Valid Token")
                            this.success = true
                        }
                    })
            } catch (err) {
                console.log("Invalid Token")
                console.log(err)
                this.fail = true
                this.success = false
            }
        },
    },
};
</script>
<style scoped>
</style>