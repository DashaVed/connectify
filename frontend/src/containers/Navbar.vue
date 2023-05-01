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
import {useAuthStore} from "@/stores/auth";
import {mapState} from "pinia";

export default {
    name: "Navbar",
    computed: {
        ...mapState(useAuthStore, ['isAuth'])
    }
}
</script>

<style scoped>
</style>