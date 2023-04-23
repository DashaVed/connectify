<template>
    <p>{{ user.first_name }}</p>
    <w-image :src="url"></w-image>
</template>

<script>
import {getUser} from "@/services/api";
import {BASE_URL} from "@/services/consts";


export default {
    name: "UserInfo",
    async created() {
        await this.load();
        await this.getUrl();
    },
    data() {
        return {
            user: null,
            url: null,
        }
    },
    methods: {
        async load() {
            this.user = await getUser(this.$route.params.id);
        },
        getUrl() {
            this.url = BASE_URL + this.user.image
        },
    }
}
</script>

<style scoped>

</style>