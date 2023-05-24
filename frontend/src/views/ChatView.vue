<script setup>
import Navbar from "@/containers/Navbar.vue";
</script>

<template>
  <Navbar />
  <div v-if="username">{{ username }}</div>
  <w-form @submit.prevent="sendMessage">
    <w-input v-model="message"
             placeholder="Введите сообщение.."></w-input>
    <w-button type="submit">Отправить</w-button>
  </w-form>

  <div>{{ messages }}</div>
</template>

<script>
import { initChat } from "@/services/websockets";
import { useAuthStore } from "@/stores/auth";
import { mapState } from "pinia";

export default {
  name: "ChatView",
  async created() {
    await this.connect();
  },
  data() {
    return {
      message: null,
      messages: "",
      username: "test",
    };
  },
  computed: {
    ...mapState(useAuthStore, ["user"]),
  },
  methods: {
    getRoomId() {
      let room;
      const sender = this.user.id;
      const receiver = this.$route.params.id;
      if (receiver > sender) {
        room = `${receiver}-${sender}`;
      } else if (receiver < sender) {
        room = `${sender}-${receiver}`;
      } else {
        this.$router.push({ name: "home" });
        return;
      }
      return room;
    },
    connect() {

      this.send = initChat(this.getRoomId(), (message) => {
        this.username = message.username;
        this.messages += message.message + "\n";
      });
    },
    sendMessage() {
      this.send({user_id: this.$route.params.id, message: this.message });
      this.message = null;
    }
  }
};
</script>

<style scoped>

</style>