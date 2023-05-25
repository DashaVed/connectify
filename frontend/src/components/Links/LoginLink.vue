<template>
<router-link :to="{name: 'login'}" class="login-button blue-dark6">Войти</router-link>
</template>

<script>
export default {
    name: "LoginButtonInHeader",
}
</script>

<style scoped>
.login-button {
    margin-right: 24px;
    /*color: var(--color-text);*/
}
.login-button:hover, .login-button:visited, .login-button:focus {
    text-decoration: underline;
}
</style>