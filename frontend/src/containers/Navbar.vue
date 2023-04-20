<script setup>
import HeaderOnlyWithTitle from "@/components/HeaderOnlyWithTitle.vue";
import LoginLink from "@/components/Links/LoginLink.vue";
import RegisterButton from "@/components/buttons/RegisterButton.vue";
</script>

<template>
    <header>
        <HeaderOnlyWithTitle>
            <LoginLink/>
            <RegisterButton md route="/register" class="pa4"/>
        </HeaderOnlyWithTitle>

    </header>
</template>

<script>
export default {
    name: "Navbar",
}
</script>

<style scoped>
</style>