<script setup>
import Navbar from "@/containers/Navbar.vue";
</script>

<template>
    <Navbar/>
    <w-button bg-color="light-blue-dark3" color="white" lg>first color</w-button>
    <w-button bg-color="light-green-dark3" color="white" lg>second color</w-button>
    <w-button bg-color="lime-light4" lg class="ma15">third color</w-button>
</template>

<script>
export default {
    name: "HomeView",
}
</script>

<style scoped>

</style>