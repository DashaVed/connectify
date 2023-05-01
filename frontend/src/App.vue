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
    mounted() {
        setInterval(() => {
            this.refreshToken()
        }, 60000)
    },
    methods: mapActions(useAuthStore, ['refreshToken'])
}
</script>

<style scoped>
</style>
