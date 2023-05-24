<script setup>
import {RouterView} from 'vue-router'
</script>

<template>
    <RouterView/>
</template>

<script>
import {useAuthStore} from "@/stores/auth";
import {mapActions} from "pinia";
import { useCategoriesStore } from "@/stores/categories";

export default {
    name: "App",
    created() {
        this.load();
        this.loadCategories();
    },
    mounted() {
        setInterval(() => {
            this.refreshToken()
        }, 3500000)
    },
    methods: {
      ...mapActions(useAuthStore, ['refreshToken', 'load']),
      ...mapActions(useCategoriesStore, ['loadCategories'])
    }
}
</script>

<style scoped>
</style>
