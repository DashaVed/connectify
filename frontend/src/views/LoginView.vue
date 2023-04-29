<script setup>
import HeaderOnlyWithTitle from "@/components/HeaderOnlyWithTitle.vue";
import LoginForm from '@/containers/forms/LoginForm.vue'
</script>

<template>
    <HeaderOnlyWithTitle/>
    <div class="box justify-center align-self-center mt10">
        <LoginForm/>
    </div>
</template>

<script>
export default {
    name: "LoginView",
}
</script>

<style>
.box {
    max-width: 400px;
}
</style>
