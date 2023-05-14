<template>
    <div class="box xs8 pl12 pt8" v-if="isLoading">
        <w-flex wrap class="mb8">
            <w-image :src="user.image" height="200" width="200"></w-image>
            <w-flex column>
                <span class="fullname__info ml10">{{user.name}}</span>
                <span class="created-at__info ml10 mb4 body">Участник с {{user.created_at}}</span>
                <span class="city__info">
                    <w-icon color="deep-orange pb1 ml10">mdi mdi-city</w-icon>
                    {{user.city}}
                </span>
            </w-flex>
        </w-flex>
        <span class="description__title">О себе</span>
        <p class="body mt2">{{user.description}}</p>
    </div>
</template>

<script>
import {getUser} from "@/services/userApi";


export default {
    name: "UserInfo",
    async created() {
        await this.load();
    },
    data() {
        return {
            user: null,
            isLoading: false,
        }
    },
    methods: {
        async load() {
            this.isLoading = false;
            this.user = await getUser(this.$route.params.id);
            this.isLoading = true;
        },
    }
}
</script>

<style scoped>
.fullname__info {
    font-size: 36px;
}
.description__title {
    font-size: 26px;
}
</style>