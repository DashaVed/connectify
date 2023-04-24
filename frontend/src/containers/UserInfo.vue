<template>
    <div class="box xs8 pl12 pt8" v-if="isLoading">
        <w-flex wrap class="mb8">
            <w-image :src="url" height="200" width="200"></w-image>
            <w-flex column>
                <span class="fullname__info ml10">{{getFullname}}</span>
                <span class="created-at__info ml10 mb8 title3">Участник с {{user.created_at}}</span>
                <span class="city__info">
                    <w-icon color="deep-orange pb1 ml10">mdi mdi-city</w-icon>
                    {{user.city}}
                </span>
            </w-flex>
        </w-flex>
        <span class="description__title">О себе</span>
        <p class="title4 mt2">{{user.description}}</p>
    </div>
</template>

<script>
import {getUser} from "@/services/api";
import {BASE_URL} from "@/services/consts";


export default {
    name: "UserInfo",
    async created() {
        await this.load();
        await this.getUrl();
    },
    data() {
        return {
            user: null,
            url: null,
            isLoading: false,
        }
    },
    computed: {
      getFullname() {
          return `${this.user.first_name} ${this.user.last_name}`
      }
    },
    methods: {
        async load() {
            this.isLoading = false;
            this.user = await getUser(this.$route.params.id);
            console.log(this.user);
            this.isLoading = true;
        },
        getUrl() {
            this.url = BASE_URL + this.user.image
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