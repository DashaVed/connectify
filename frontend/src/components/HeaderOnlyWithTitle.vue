<template>
    <header>
        <w-toolbar shadow>
            <router-link :to="{name: 'main'}">
                <div class="title1 text-bold blue-dark6">Connectify</div>
            </router-link>
            <div class="spacer"></div>
            <slot></slot>
        </w-toolbar>
    </header>
</template>

<script>

export default {
    name: "HeaderOnlyWithTitle",
}
</script>

<style scoped>

</style>