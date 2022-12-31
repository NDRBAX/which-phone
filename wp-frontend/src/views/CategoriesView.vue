<template>
  <div class="flex min-h-full items-center justify-center py-12">
    <CustomLoader v-if="isLoading" />
    <div class="w-full space-y-8">
      <div>
        <h2
          class="text-center sm:text-2xl md:text-3xl lg:text-4xl text-4xl font-bold tracking-tight text-gray-900"
        >
          Search by <span class="text-teal-accent-400">categorie</span>
        </h2>
        <p class="mt-2 text-center text-lg text-gray-600">
          You have not added any phones to your wishlist yet. Make a search to
          find phones you like and add them to your wishlist.
        </p>
      </div>

      <div
        id="categories"
        class="bg-gradient-to-tr from-teal-accent-400 to-blue bg-white mb-20 animated-gradient px-0 sm:px-0 lg:px-0"
      >
        <div
          class="relative px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-20"
        >
          <div
            class="relative grid gap-5 xs:grid-cols-3 sm:grid-cols-3 lg:grid-cols-6"
          >
            <div
              v-for="item in categories"
              :key="item.title"
              class="px-10 py-20 bg-gray-600 bg-blend-multiply text-center transition duration-300 transform rounded shadow-2xl hover:scale-105 md:shadow-xl hover:shadow-2xl"
              v-bind:style="{
                backgroundImage: 'url(' + item.coverImage + ')',
                backgroundSize: 'cover',
                backgroundPosition: 'center',
              }"
              @click="receiveData(item.title)"
            >
              <p class="font-semibold text-gray-200 sm:text-lg lg:text-base">
                {{ item.title }}
              </p>
            </div>
          </div>
        </div>
      </div>
      <div class="pt-8"><CategoryFilters v-bind:data="devices" /></div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { inject } from "vue";
import CategoryFilters from "../components/CategoryFilters.vue";
import CustomLoader from "../components/CustomLoader.vue";

export default {
  name: "CategoriesView",
  components: {
    CategoryFilters,
    CustomLoader,
  },
  data() {
    return {
      categories: inject("dataENG").categories,
      data: false,
      token: localStorage.getItem("csrfToken"),
      isLoading: false,
      devices: [],
    };
  },

  methods: {
    async receiveData(category) {
      this.isLoading = true;
      const url = "/wphone/get_categories";
      const data = {
        category: category,
      };

      const config = {
        headers: {
          "Content-Type": "application/json",
        },
      };

      await axios
        .post(url, data, config)
        .then((response) => {
          this.devices = [...response.data];
          console.log(this.devices);
          this.data = true;
          this.isLoading = false;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
