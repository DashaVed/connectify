<template>
    <w-button
            type="submit"
            class="pa4"
            disabled sm>
        <slot></slot>
    </w-button>
</template>

<script>
export default {
    name: "DisabledButton"
}
</script>

<style scoped>
</style>