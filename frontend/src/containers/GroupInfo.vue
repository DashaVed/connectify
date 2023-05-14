<script setup>
import {default as EnterButton} from '@/components/buttons/OrangeButton.vue'
</script>

<template>
    <div class="content mx12 my12" v-if="isLoading">
        <w-flex wrap gap="2" class="justify-space-between">
            <div class="box ml12">
                <div class="title1 text-bold mb8">{{group.title}}</div>
                <div class="body">
                    <w-icon color="deep-orange pb1">mdi mdi-city</w-icon>
                    {{group.city}}</div>
                <div class="body mb8">
                    <w-icon color="deep-orange pb1">mdi mdi-account-group</w-icon>
                    Участников - {{countUsers}}</div>
                <div class="title3">Про что группа?</div>
                <p class="body my4">{{group.description}}</p>
            </div>
            <div class="box mr12">
                <EnterButton>Вступить в группу</EnterButton>
                <div class="title3 my8 text-right">Организатор</div>
                <div class="body">{{admin}}</div>
                <div class="title3 my8 text-right">Участники ({{countUsers}})</div>
            </div>
        </w-flex>

    </div>
</template>

<script>
import {getGroup} from "@/services/groupApi";

export default {
    name: "GroupInfo",
    async created() {
        await this.loadGroup()
    },
    data() {
        return {
            group: null,
            isLoading: false,
        }
    },
    computed: {
        countUsers() {
            return this.group.users.length
        },
        admin() {
            for (const user of this.group.users) {
                console.log(user)
                if (user.role === "admin") {
                    return user.user
                }
            }
        }
    },
    methods: {
        async loadGroup() {
            this.isLoading = false;
            this.group = await getGroup(this.$route.params.id);
            this.isLoading = true;
        }
    }
}
</script>

<style scoped>

</style>