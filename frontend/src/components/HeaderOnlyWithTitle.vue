<template>
  <header>
    <w-toolbar shadow>
      <router-link :to="{name: 'main'}" v-if="!isAuth">
        <div class="title2 text-bold blue-dark6">Connectify</div>
      </router-link>
      <router-link :to="{name: 'home'}" v-if="isAuth">
        <div class="title2 text-bold blue-dark6">Connectify</div>
      </router-link>
      <div class="spacer"></div>
      <slot></slot>
    </w-toolbar>
  </header>
</template>

<script>

import {useAuthStore} from "@/stores/auth";
import {mapState} from "pinia";

export default {
  name: "HeaderOnlyWithTitle",
  computed: {
    ...mapState(useAuthStore, ["isAuth"]),
  }
}
</script>

<style scoped>

</style>