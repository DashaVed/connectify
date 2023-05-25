<script setup>
import Navbar from "@/containers/Navbar.vue";
</script>

<template>
  <Navbar />
  <main>
    <w-flex column class="align-center justify-space-beetwen">
      <div class="ma12" style="font-size:40px">Connectify</div>
      <div class="my4" style="width: 600px">Cервис, который помогает людям искать единомышленников,
        проводить тематические встречи и реализовывать свой потенциал!</div>
    </w-flex>
  </main>
</template>

<script>
export default {
  name: "HomeView"
};
</script>

<style scoped>

</style>