<template>
    <div class="container">
        <h1>Point At QR Code</h1>
        <div>
            <center>
                <QRReader style="height: 400px; width: 400px"></QRReader>
            </center>
        </div>
        <div>
            <button>Logout</button>
            <button>Help</button>
        </div>
    </div>
</template>
<script>
import QRReader from "../components/QRReader.vue";

export default {
    components: {QRReader}
}
</script>