<template>
    <header>
        <w-toolbar shadow>
            <div class="title1 text-bold">Connectify</div>
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