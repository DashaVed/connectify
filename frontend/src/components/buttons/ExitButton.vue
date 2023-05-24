<template>
  <w-confirm sm bg-color='grey-light1' color="white" class="pa4 mt4"
  cancel="Нет" confirm="Да">
    <slot></slot>
  </w-confirm>
</template>

<script>
export default {
  name: "DisabledButton"
};
</script>

<style scoped>
</style>