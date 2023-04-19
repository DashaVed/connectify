<script>
import LoginButtonInHeader from "@/components/buttons/LoginButtonInHeader.vue";
import RegisterButton from "@/components/buttons/RegisterButton.vue";
export default {
    name: "Navbar",
    components: {LoginButtonInHeader, RegisterButton},
}
</script>

<template>
    <header>
        <w-toolbar shadow>
            <div class="title1 text-bold">Connectify</div>
            <div class="spacer"></div>
            <LoginButtonInHeader/>
            <RegisterButton md route="/register" class="pa4"/>
        </w-toolbar>
    </header>
</template>

<style scoped>
</style>