<script setup>
import { default as EnterButton } from "@/components/buttons/OrangeButton.vue";
import Navbar from "@/containers/Navbar.vue";
</script>

<template>
  <Navbar />
  <w-flex column class="justify-start mt12">
    <div class="box align-self-center">
      <w-card class="chat-content pa4" tile>
      <template #title>
        <w-toolbar>
          <div class="title3">{{ username }}</div>
        </w-toolbar>
      </template>
      <w-card class="chat-messages mt4">
        <p>{{ messages }}</p>
      </w-card>
            <w-form @submit.prevent="sendMessage">
        <w-flex class="mt4 align-center justify-space-between">
          <w-input v-model="message" outline class="py8"
                   placeholder="Введите сообщение.."></w-input>
          <EnterButton class="ml8">Отправить</EnterButton>
        </w-flex>
      </w-form>
    </w-card>
    </div>


  </w-flex>
  <p>{{ messages }}</p>
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
      username: this.$route.query.username
    };
  },
  computed: {
    ...mapState(useAuthStore, ["user"])
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
      this.send({ user_id: this.$route.params.id, message: this.message });
      this.message = null;
    }
  }
};
</script>

<style scoped>
.chat-content {
  min-width: 800px;
}
.chat-messages {
  height: 200px;
  max-height: 200px;
  overflow-y: scroll;
}
</style>