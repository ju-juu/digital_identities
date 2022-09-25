<template>
    <div class="container">
        <h1>Point At QR Code</h1>
        <div>
            <center>
                <QRReader style="height: 400px; width: 400px"></QRReader>
            </center>
        </div>
    </div>
</template>
<script>
import AuthorityScanner from "./AuthorityScanner.vue";
import QRReader from "../components/QRReader.vue";

export default {
    components: {QRReader, AuthorityScanner}
}
</script>