<script setup>
import {RouterView} from 'vue-router'
</script>

<template>
    <RouterView/>
</template>

<script>
import {useAuthStore} from "@/stores/auth";
import {mapActions} from "pinia";

export default {
    name: "App",
    created() {
        this.load();
    },
    mounted() {
        setInterval(() => {
            this.refreshToken()
        }, 175000)
    },
    methods: mapActions(useAuthStore, ['refreshToken', 'load'])
}
</script>

<style scoped>
</style>
