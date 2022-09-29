<template>
    <div class="container">
        <h1>Help</h1>
        <div>
            <center>
                <br>
                <br>
                <section>
                    What is Lorem Ipsum?
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
                </section>
                <br>
                <br>
            </center>
        </div>
        <div>
            <button class="button button2" @click="back()" style="width: 100%" align="center">Back</button>
        </div>
    </div>
</template>
<script>
import router from "../router";
export default {
    name: 'AuthorityHelp',
    methods: {
        back() {
            router.push('/authority_home')
        },
    },
}
</script>