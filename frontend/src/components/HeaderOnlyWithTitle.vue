<template>
  <header>
    <w-toolbar class="py2" shadow>
      <w-flex wrap gap="2">
        <router-link :to="{name: 'main'}" v-if="!isAuth" class="xs2">
          <div class="title2 text-bold blue-dark6">Connectify</div>
        </router-link>
        <router-link :to="{name: 'home'}" v-if="isAuth" class="xs2">
          <div class="title2 text-bold blue-dark6">Connectify</div>
        </router-link>
        <slot></slot>
      </w-flex>

    </w-toolbar>
  </header>
</template>

<script>

import { useAuthStore } from "@/stores/auth";
import { mapState } from "pinia";

export default {
  name: "HeaderOnlyWithTitle",
  computed: {
    ...mapState(useAuthStore, ["isAuth"])
  }
};
</script>

<style scoped>

</style>