<script setup>
import RegistrationForm from "@/containers/forms/RegistrationForm.vue";
import HeaderOnlyWithTitle from "@/components/HeaderOnlyWithTitle.vue";
</script>

<template>
    <HeaderOnlyWithTitle/>
    <div class="box justify-center align-self-center mt10">
        <RegistrationForm/>
    </div>
</template>

<script>

export default {
    name: "RegistrationView",
}
</script>

<style>
.box {
    width: 400px;
}
</style>
