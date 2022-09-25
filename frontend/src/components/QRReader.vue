<template>
    <div class="hello">
        <StreamBarcodeReader
            @decode="(a, b, c) => onDecode(a, b, c)"
            @loaded="() => onLoaded()"
        ></StreamBarcodeReader>
        <div v-if="qrCode">
            <button @click="validateQRCode()" v-if="qrCode">Validate</button>
        </div>
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
            axios
                .post("/validate_token", {}, {
                    headers: {
                        'Authorization': 'Bearer ' + this.qrCode
                    },
                }).then(response => console.log(response)) // #TODO if response code == 200 display tick, else cross
        },
    },
};
</script>
<style scoped>
</style>