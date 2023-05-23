import { defineStore } from "pinia";
import { getCategories } from "@/services/groupApi";

export const useCategoriesStore = defineStore("categories", {
  state: () => {
    return {
      categories: [],
    };
  },
  actions: {
    async loadCategories() {
      let response = await getCategories();
      response = response.data.results;
      for (let i = 0; i < response.length; i++) {
        this.categories.push({ label: response[i].title, value: response[i].id });
      }
    }
  }
});