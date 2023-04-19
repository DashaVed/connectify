<template>
<a href="/login" class="login-button">Войти</a>
</template>

<script>
export default {
    name: "LoginButtonInHeader"
}
</script>

<style scoped>
.login-button {
    margin-right: 14px;
    color: var(--color-text);
}
.login-button:hover, .login-button:visited, .login-button:focus {
    text-decoration: underline;
    color: var(--color-text);
}
</style>