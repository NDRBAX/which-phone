<template>
  <!--  -->
  <section
    v-if="hasToken"
    class="relative mx-auto xs:max-w-xl sm:max-w-xl md:max-w-3xl lg:max-w-4xl xl:max-w-6xl"
  >
    <div
      v-if="itemsOnCurrentPage.length > 0"
      class="flex min-h-full items-center justify-center py-12 px-4 sm:px-6 lg:px-8"
    >
      <div class="w-full max-w-md space-y-8">
        <div>
          <h2
            class="text-center sm:text-2xl md:text-3xl lg:text-4xl text-4xl font-bold tracking-tight text-gray-900"
          >
            Your <span class="text-teal-accent-400">wishlist</span>
          </h2>
          <p class="mt-2 text-center text-lg text-gray-600">
            Here you can see all the phones you have added to your wishlist.
          </p>
        </div>
      </div>
    </div>
    <!-- Card Grid -->
    <div
      v-if="itemsOnCurrentPage.length > 0"
      class="grid grid-flow-row gap-8 text-neutral-600 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4"
    >
      <!-- Card Item -->
      <div
        v-for="item of itemsOnCurrentPage"
        :key="item.device_id"
        class="flex flex-col justify-center items-center max-w-xs mx-auto my-4"
      >
        <PhoneCard
          :device_id="item.device_id"
          :name="item.name"
          :price="item.price"
          :thumbnail="item.thumbnail"
          :summary="item.summary"
          :battery="item.battery"
          :camera="item.camera"
          :screen="item.screen"
          :ram="item.ram"
          :storage="item.storage"
          :selfie="item.selfie"
          :musicplay="item.musicplay"
          :talktime="item.talktime"
          :standby="item.standby"
          :inWishlist="inWishlist(item.device_id)"
        />
      </div>
    </div>
    <div v-if="empty">
      <div
        class="flex min-h-full items-center justify-center py-12 px-4 sm:px-6 lg:px-8"
      >
        <div class="w-full max w-md space-y-8">
          <div>
            <h2
              class="text-center sm:text-2xl md:text-3xl lg:text-4xl text-4xl font-bold tracking-tight text-gray-900"
            >
              Your <span class="text-teal-accent-400">wishlist</span> is empty
            </h2>
            <p class="mt-2 text-center text-lg text-gray-600">
              You have not added any phones to your wishlist yet. Make a search
              to find phones you like and add them to your wishlist.
            </p>
          </div>

          <div class="flex justify-center">
            <router-link to="/search">
              <button
                class="inline-flex items-center justify-center xs:w-20 xs:h-10 xs:text-sm sm md sm:w-44 sm:h-12 px-6 font-medium tracking-wide text-white transition duration-200 rounded shadow-md bg-teal-accent-400 enabled:hover:bg-teal-accent-600 focus:shadow-outline focus:outline-none ml-4"
              >
                Search
              </button>
            </router-link>
          </div>
        </div>
      </div>
    </div>
    <div class="grid grid-cols-7 mt-14" v-if="totalPages > 1">
      <div
        class="btn-group grid xs:col-start-2 xs:col-span-5 grid-cols-3 sm:col-start-2 sm:col-span-5 xs:text-sm sm:text-base"
        data-theme="dark"
      >
        <button
          class="btn btn-outline btn-success"
          v-on:click="previousPage"
          :disabled="currentPage === 1"
        >
          Previous
        </button>
        <button class="btn disabled">
          Page {{ currentPage }} of {{ totalPages }}
        </button>
        <button class="btn btn-outline btn-success" v-on:click="nextPage">
          Next
        </button>
      </div>
    </div>
  </section>

  <section v-else>
    <div
      class="flex min-h-full items-center justify-center py-12 px-4 sm:px-6 lg:px-8"
    >
      <div class="w-full max w-md space-y-8">
        <div>
          <h2
            class="text-center sm:text-2xl md:text-3xl lg:text-4xl text-4xl font-bold tracking-tight text-gray-900"
          >
            Your <span class="text-teal-accent-400">wishlist</span>
          </h2>
          <p class="mt-2 text-center text-lg text-gray-600 px-12">
            To add phones to your wishlist or to see your wishlist, you need to
            be logged in. If you don't have an account, you can register here.
          </p>
        </div>

        <div class="flex justify-center">
          <router-link to="/register">
            <button
              class="inline-flex items-center justify-center xs:w-20 xs:text-sm sm md sm:w-44 sm:h-12 xs:h-10 px-6 font-medium tracking-wide text-gray-900 bg-white ring-inset ring-2 ring-gray-900 enabled:hover:ring-0 enabled:hover:bg-gray-900 enabled:hover:text-white transition duration-200 rounded shadow-md focus:shadow-outline focus:outline-none"
            >
              Register
            </button>
          </router-link>
          <router-link to="/login">
            <button
              class="inline-flex items-center justify-center xs:w-20 xs:h-10 xs:text-sm sm md sm:w-44 sm:h-12 px-6 font-medium tracking-wide text-white transition duration-200 rounded shadow-md bg-teal-accent-400 enabled:hover:bg-teal-accent-600 focus:shadow-outline focus:outline-none ml-4"
            >
              Login
            </button>
          </router-link>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { useWishlistStore } from "../stores/checked";
import PhoneCard from "../components/PhoneCard.vue";

export default {
  name: "WishListView",
  components: {
    PhoneCard,
  },
  data() {
    return {
      currentPage: 1,
      itemsPerPage: 8,
      store: useWishlistStore(),
      dataWishlist: [],
    };
  },
  computed: {
    totalPages() {
      return Math.ceil(this.dataWishlist.length / this.itemsPerPage);
    },
    itemsOnCurrentPage() {
      const startIndex = (this.currentPage - 1) * this.itemsPerPage;
      return this.dataWishlist.slice(
        startIndex,
        startIndex + this.itemsPerPage
      );
    },
    hasToken() {
      return localStorage.getItem("access");
    },
    inWishlist() {
      return (device_id) => this.store.getIdWishlist.includes(device_id);
    },
    empty() {
      return this.store.getWishlist.length === 0;
    },
  },
  created() {
    if (this.hasToken) {
      this.store.initializeWishlist();
      this.dataWishlist = this.store.getWishlist;
      console.log(this.inWishlist);

      if (this.dataWishlist.length > 0) {
        this.dataWishlist = this.dataWishlist.filter(
          (thing, index, self) =>
            index === self.findIndex((t) => t.device_id === thing.device_id)
        );
      }
    }
  },

  methods: {
    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    },
    closeMessageError() {
      this.errors = [];
    },
  },
  beforeUnmount() {
    this.store.saveToDB();
    this.store.clearWishlist();
  },
};
</script>
